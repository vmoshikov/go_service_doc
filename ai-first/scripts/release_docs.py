#!/usr/bin/env python3
"""Документация релиза платформы по тегу репозитория чартов.

Использование:
    python scripts/release_docs.py <путь_к_репозиторию_чартов> <тег> [--previous <тег>] [--repos-dir <каталог>] [--all]

Репозиторий чартов должен стоять на теге релиза. Скрипт:
  1. Читает состав: версию чарта и тег образа каждого компонента.
  2. Сравнивает состав с предыдущим тегом.
  3. Пишет config.md каждого компонента из values.yaml и значений платформы.
  4. Код компонентов документирует code_docs.py на каждый тег компонента. Здесь — только недостающие версии,
     если тег в релизе новее, чем в wiki. Более старую версию скрипт не перезаписывает: он даёт ссылку
     на коммит wiki, где эта версия была сгенерирована.
  5. Пишет wiki/code/releases/<тег>.md: состав, ссылки на документацию версий, модули, изменения.
  6. Обновляет wiki/index.md и пишет событие в wiki/log.md.

Скил: skills/release-docs/SKILL.md
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

import _helm
import _config
import _llm
import code_docs
import wiki_index
from code_docs import checkout, documented_version, git_ref, version_key
from _wiki import CODE, RELEASES, ROOT, append_log, frontmatter, git, load_registry, read_page



# ---------- Чтение репозитория чартов ----------

def read_at(charts: Path, ref, path: str):
    """Текст файла: из рабочей копии (ref=None) или из git на ref. None, если файла нет."""
    if ref is None:
        file = charts / path
        return file.read_text(encoding="utf-8") if file.is_file() else None
    return git("show", f"{ref}:{path}", cwd=charts)


def yaml_at(charts, ref, path):
    text = read_at(charts, ref, path)
    return (yaml.safe_load(text) or {}) if text is not None else None


def composition(charts: Path, ref, registry) -> dict:
    """{компонент: {"chart_version", "tag"}} на ref. ref=None — рабочая копия."""
    result = {}
    for name, entry in registry["components"].items():
        chart = yaml_at(charts, ref, f"{entry['chart']}/Chart.yaml")
        if chart is None:
            continue  # компонента ещё не было в этом релизе
        file, dotted = _helm.split_ref(entry.get("tag", f"{entry['chart']}/values.yaml#image.tag"))
        tag = _helm.dig(yaml_at(charts, ref, file) or {}, dotted)
        result[name] = {"chart_version": str(chart.get("version", "?")), "tag": str(tag) if tag else None}
    return result


def check_registry(charts: Path, registry) -> list:
    """Ошибки: чарт без записи в реестре, запись без чарта, нет тега образа."""
    errors = []
    known = {entry["chart"].rstrip("/") for entry in registry["components"].values()}
    for chart_file in sorted(charts.glob("**/Chart.yaml")):
        chart_dir = chart_file.parent
        if any((p / "Chart.yaml").is_file() for p in chart_dir.parents if charts in p.parents or p == charts):
            continue  # зависимость внутри другого чарта
        rel = chart_dir.relative_to(charts).as_posix()
        if rel not in known:
            errors.append(f"чарт {rel} не описан в wiki/code/components.toml")
    for name, entry in registry["components"].items():
        if not (charts / entry["chart"] / "Chart.yaml").is_file():
            errors.append(f"{name}: нет чарта {entry['chart']}")
    return errors


# ---------- config.md ----------

def write_config(name, entry, charts: Path, release, info) -> None:
    values_file = f"{entry['chart']}/values.yaml"
    text = read_at(charts, None, values_file) or ""
    values = yaml.safe_load(text) or {}
    comments = _helm.value_comments(text)
    overrides, override_ref = {}, entry.get("overrides")
    if override_ref:
        file, dotted = _helm.split_ref(override_ref)
        overrides = _helm.dig(yaml_at(charts, None, file) or {}, dotted) or {}

    defaults = dict(_helm.flatten(values))
    platform = dict(_helm.flatten(overrides))
    out = CODE / name
    out.mkdir(parents=True, exist_ok=True)
    body = [
        frontmatter(title=f"{name} — конфигурация чарта", type="code-config", components=[name],
                    chart=entry["chart"], chart_version=info["chart_version"], release=release,
                    generated="true"),
        f"# {name} — конфигурация чарта\n",
        f"Чарт `{entry['chart']}` версии `{info['chart_version']}` в платформе `{release}`. "
        f"Тег образа: `{info['tag']}`.",
    ]
    if override_ref:
        body.append(f"Значения платформы: `{override_ref}`.")
    body += ["", "Колонка «Платформа» заполнена, если сборка платформы меняет значение чарта.", "",
             "| Параметр | По умолчанию | Платформа | Описание |",
             "|----------|--------------|-----------|----------|"]
    for key in list(defaults) + [k for k in platform if k not in defaults]:
        body.append(f"| `{key}` | {_helm.show(key, defaults.get(key))} | "
                    f"{_helm.show(key, platform[key]) if key in platform else ''} | {comments.get(key, '—')} |")
    (out / "config.md").write_text("\n".join(body) + "\n", encoding="utf-8")


# ---------- Репозитории компонентов ----------

def readme_rel(name) -> str:
    path = CODE / name / "README.md"
    return path.relative_to(ROOT).as_posix() if ROOT in path.parents else f"wiki/code/{name}/README.md"


def version_commit(name, version):
    """(коммит, текст README) последней генерации этой версии в истории wiki или (None, None)."""
    path = readme_rel(name)
    for sha in (git("log", "--format=%H", f"-Sversion: {version}", "--", path, cwd=ROOT) or "").split():
        text = git("show", f"{sha}:{path}", cwd=ROOT) or ""
        if f"\nversion: {version}\n" in text:
            return sha[:12], text
    return None, None


def changelog_section(name, version) -> str:
    path = CODE / name / "CHANGELOG.md"
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    start = text.find(f"## [{version}]")
    if start < 0:
        return ""
    end = text.find("\n## [", start + 1)
    section = text[start:end if end > 0 else None].strip()
    section = section.split("\n", 1)[1].strip() if "\n" in section else ""
    return re.sub(r"^(#+) ", r"#\1 ", section, flags=re.M)  # ### → ####


# ---------- Точка входа ----------

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Документация релиза платформы.")
    parser.add_argument("charts", type=Path, help="репозиторий чартов на теге релиза")
    parser.add_argument("tag", help="тег релиза — версия платформы")
    parser.add_argument("--previous", help="предыдущий тег; по умолчанию ближайший тег до текущего")
    parser.add_argument("--repos-dir", type=Path, default=Path(".repos"), help="кэш клонов компонентов")
    parser.add_argument("--all", action="store_true", help="перегенерировать компоненты и модули по версиям релиза")
    parser.add_argument("--no-llm", action="store_true", help="только факты, без текста LLM")
    args = parser.parse_args(argv)

    charts = args.charts.resolve()
    head_tags = (git("tag", "--points-at", "HEAD", cwd=charts) or "").split()
    if args.tag not in head_tags:
        print(f"Ошибка: репозиторий чартов не стоит на теге {args.tag}. Выполни git checkout {args.tag}.",
              file=sys.stderr)
        return 1

    registry = load_registry()
    errors = check_registry(charts, registry)
    current = composition(charts, None, registry)
    errors += [f"{n}: не найден тег образа" for n, i in current.items() if not i["tag"]]
    if errors:
        print("\n".join(f"ОШИБКА  {e}" for e in errors), file=sys.stderr)
        return 1

    previous_tag = args.previous or git("describe", "--tags", "--abbrev=0", f"{args.tag}^", cwd=charts)
    previous = composition(charts, previous_tag, registry) if previous_tag else {}
    repos_dir = args.repos_dir.resolve()
    repos_dir.mkdir(parents=True, exist_ok=True)

    client = _llm.Client(enabled=not args.no_llm)
    cfg = _config.load()
    blob = f"{cfg['gitlab']['url'].rstrip('/')}/{cfg['gitlab']['wiki_project']}/-/blob"
    changed, docs = [], {}

    def document(name, version, repo_url, crd_dirs=()):
        """Ссылка на документацию версии. Генерирует её, если wiki описывает более старую версию."""
        documented = documented_version(name)
        if args.all or documented is None or version_key(version) > version_key(documented):
            repo = checkout(repos_dir, name, repo_url, git_ref(version))
            code_docs.generate(repo, name, version, documented, crd_dirs=crd_dirs, registry=registry, llm=client)
            changed.append(name)
            return f"[текущая](../{name}/README.md)", read_page(CODE / name / "README.md")
        if documented == version:
            return f"[текущая](../{name}/README.md)", read_page(CODE / name / "README.md")
        sha, text = version_commit(name, version)
        if not sha:
            return "нет документации версии", None
        return f"[коммит {sha}]({blob}/{sha}/{readme_rel(name)})", read_page(CODE / name / "README.md", text)

    pages_meta = {}
    for name, info in current.items():
        entry = registry["components"][name]
        write_config(name, entry, charts, args.tag, info)
        docs[name], pages_meta[name] = document(name, info["tag"], entry["repo"], [charts / entry["chart"] / "crds"])

    # Модули: самая новая версия, которую использует хотя бы один компонент релиза.
    used_by = {}
    for name in current:
        for item in (pages_meta[name].values("uses") if pages_meta[name] else []):
            module, _, version = item.rpartition("@")
            used_by.setdefault(module, []).append((name, version))
    module_rows = []
    for name, entry in registry["modules"].items():
        users = sorted(used_by.get(entry["module"], []))
        if not users:
            module_rows.append(f"| {name} | — | не используется | — |")
            continue
        target = max((v for _, v in users), key=version_key)
        link, _ = document(name, target, entry["repo"])
        skew = " · ⚠ разные версии" if len({v for _, v in users}) > 1 else ""
        module_rows.append(f"| {name} | `{target}` | " + ", ".join(f"{u} `{v}`" for u, v in users) + skew
                           + f" | {link} |")

    # Страница релиза.
    RELEASES.mkdir(parents=True, exist_ok=True)
    body = [
        frontmatter(title=f"Релиз платформы {args.tag}", type="release", components=sorted(current),
                    version=args.tag, previous=previous_tag, generated="true"),
        f"# Релиз платформы {args.tag}\n",
        f"Предыдущий релиз: `{previous_tag}`." if previous_tag else "Первый документированный релиз.",
        "",
        "## Состав\n",
        "Документация версии — wiki на момент генерации этого тега. «текущая» — тег совпадает с последним в wiki.",
        "",
        "| Компонент | Чарт | Образ | Было | Документация версии |",
        "|-----------|------|-------|------|---------------------|",
    ]
    for name, info in sorted(current.items()):
        old = previous.get(name, {}).get("tag")
        was = "новый" if name not in previous else (f"`{old}`" if old != info["tag"] else "без изменений")
        body.append(f"| {name} | `{info['chart_version']}` | `{info['tag']}` | {was} | {docs[name]} |")
    removed = sorted(set(previous) - set(current))
    if removed:
        body.append("\nУдалены из платформы: " + ", ".join(f"`{n}`" for n in removed) + ".")
    if module_rows:
        body += ["", "## Модули\n", "| Модуль | Версия | Используют | Документация версии |",
                 "|--------|--------|------------|---------------------|"] + module_rows
    body.append("\n## Изменения\n")
    updated = [n for n in sorted(current) if previous.get(n, {}).get("tag") != current[n]["tag"]]
    if not updated:
        body.append("Версии компонентов не изменились.")
    for name in updated:
        body.append(f"### {name} `{current[name]['tag']}`\n")
        body.append(changelog_section(name, current[name]["tag"]) or "_Нет записи в CHANGELOG._")
        body.append("")
    (RELEASES / f"{args.tag}.md").write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")

    wiki_index.main([])
    pages = [f"code/releases/{args.tag}.md"] + [f"code/{n}/README.md" for n in changed]
    append_log("release", args.tag, pages,
               f"Изменены: {', '.join(updated) or 'нет'}. Перегенерированы: {', '.join(changed) or 'нет'}.")
    print(f"Записан wiki/code/releases/{args.tag}.md. Перегенерированы: {', '.join(changed) or 'нет'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
