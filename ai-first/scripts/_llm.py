"""Клиент OpenAI-совместимого API (Qwen, DeepSeek, внутренний LLM-шлюз) для генерации документации.

- Адрес, ключ и модель: openai.base_url, openai.api_key (или OPENAI_API_KEY), docs_llm.model или openai.model.
- Кэш ответов по хэшу запроса: неизменённый код не вызывает модель повторно и даёт тот же текст.
- Бюджет вызовов на запуск: docs_llm.max_calls. Превышение не ломает генерацию: остальное — без LLM.
- temperature 0 и JSON-ответ: результат проверяет вызывающий код.

Это модуль, а не скил: префикс «_» исключает его из проверки check_skills.py.
"""
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

import _config
from _wiki import ROOT

TIMEOUT = 120
RETRIES = 2


class LLMUnavailable(Exception):
    """Модель недоступна: нет ключа, сети или бюджета. Генерация продолжается без LLM."""


class Client:
    def __init__(self, enabled: bool = True):
        cfg = _config.load()
        settings = cfg.get("docs_llm", {})
        self.enabled = enabled and settings.get("enabled", True)
        self.model = settings.get("model") or cfg.get("openai", {}).get("model", "")
        self.base_url = (cfg.get("openai", {}).get("base_url") or "").rstrip("/")
        self.max_calls = int(settings.get("max_calls", 300))
        self.max_input = int(settings.get("max_input_chars", 24000))
        raw_cache = os.environ.get("DOCS_LLM_CACHE") or settings.get("cache_dir", ".llm-cache")
        self.cache = Path(os.path.expanduser(raw_cache))
        if not self.cache.is_absolute():
            self.cache = ROOT / self.cache
        self.calls = self.hits = 0
        self.reason = ""
        self.key = ""
        if not self.enabled:
            self.reason = "LLM выключена (--no-llm или docs_llm.enabled = false)"
        elif not self.model:
            self.reason = "не задана модель: docs_llm.model или openai.model"
        else:
            try:
                self.key = _config.secret("openai.api_key")
            except SystemExit:
                self.reason = "нет ключа: openai.api_key или OPENAI_API_KEY"

    @property
    def ready(self) -> bool:
        return not self.reason

    def ask_json(self, system: str, user: str) -> dict:
        """Ответ модели как JSON-объект. LLMUnavailable — если ответа нет."""
        if not self.ready:
            raise LLMUnavailable(self.reason)
        user = user[: self.max_input]
        body = {"model": self.model, "temperature": 0, "response_format": {"type": "json_object"},
                "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
        digest = hashlib.sha256(json.dumps(body, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        cached = self.cache / f"{digest}.json"
        if cached.is_file():
            self.hits += 1
            return json.loads(cached.read_text(encoding="utf-8"))
        if self.calls >= self.max_calls:
            raise LLMUnavailable(f"исчерпан бюджет docs_llm.max_calls = {self.max_calls}")
        self.calls += 1
        content = self._post(body)
        data = parse_json(content)
        self.cache.mkdir(parents=True, exist_ok=True)
        cached.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return data

    def _post(self, body: dict) -> str:
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions", data=json.dumps(body).encode("utf-8"), method="POST",
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.key}"})
        for attempt in range(RETRIES + 1):
            try:
                with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                    payload = json.loads(response.read())
                return payload["choices"][0]["message"]["content"]
            except urllib.error.HTTPError as exc:
                if exc.code == 400 and "response_format" in body:
                    body = {k: v for k, v in body.items() if k != "response_format"}  # сервер без JSON-режима
                    request.data = json.dumps(body).encode("utf-8")
                    continue
                if exc.code < 500 and exc.code != 429:
                    raise LLMUnavailable(f"API ответил {exc.code}") from None
            except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as exc:
                if attempt == RETRIES:
                    raise LLMUnavailable(f"нет ответа API: {exc}") from None
            time.sleep(2 * (attempt + 1))
        raise LLMUnavailable("нет ответа API")

    def summary(self) -> str:
        if not self.ready:
            return f"LLM не использована: {self.reason}"
        return f"LLM {self.model}: вызовов {self.calls}, из кэша {self.hits}"


def parse_json(text: str) -> dict:
    """JSON-объект из ответа. Модели иногда оборачивают его в ```json."""
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise LLMUnavailable("ответ модели — не JSON")
    try:
        data = json.loads(text[start:end + 1])
    except json.JSONDecodeError:
        raise LLMUnavailable("ответ модели — не JSON") from None
    if not isinstance(data, dict):
        raise LLMUnavailable("ответ модели — не объект JSON")
    return data
