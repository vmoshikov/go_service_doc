"""Клиенты Jira и GitLab по персональному токену. Только стандартная библиотека.

Токены берутся из config.json в корне репозитория или из окружения (приоритет у окружения). Токены не выводятся.
  jira.token   / JIRA_TOKEN   — Jira Data Center: Personal Access Token; Jira Cloud: API token
  jira.email   / JIRA_EMAIL   — только Jira Cloud (auth = "basic")
  gitlab.token / GITLAB_TOKEN — GitLab Personal Access Token, scope api
"""
import base64
import json
import urllib.error
import urllib.parse
import urllib.request

from _config import secret

TIMEOUT = 30


class ApiError(SystemExit):
    """Ошибка API. Наследует SystemExit: скрипт завершается с понятным сообщением."""


def _request(method: str, url: str, headers: dict, body=None, service: str = ""):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {"Accept": "application/json", **headers}
    if data is not None:
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:500]
        hint = {401: "токен неверен или истёк", 403: "у токена нет прав", 404: "объект не найден"}.get(exc.code, "")
        raise ApiError(f"Ошибка {service}: {method} {urllib.parse.urlsplit(url).path} → {exc.code}"
                       f"{' (' + hint + ')' if hint else ''}. {detail}") from None
    except urllib.error.URLError as exc:
        raise ApiError(f"Ошибка {service}: нет соединения с {urllib.parse.urlsplit(url).netloc}: {exc.reason}") from None
    return json.loads(raw) if raw else {}


# ---------- Jira ----------

class Jira:
    def __init__(self, cfg: dict):
        self.url = cfg["url"].rstrip("/")
        self.cloud = cfg.get("auth", "bearer") == "basic"
        token = secret("jira.token")
        if self.cloud:
            pair = f"{secret('jira.email')}:{token}".encode("utf-8")
            self.headers = {"Authorization": "Basic " + base64.b64encode(pair).decode("ascii")}
        else:
            self.headers = {"Authorization": f"Bearer {token}"}

    def _call(self, method, path, body=None, params=None):
        url = f"{self.url}{path}" + (f"?{urllib.parse.urlencode(params)}" if params else "")
        return _request(method, url, self.headers, body, "Jira")

    def browse(self, key: str) -> str:
        return f"{self.url}/browse/{key}"

    def myself(self) -> dict:
        me = self._call("GET", "/rest/api/2/myself")
        return {"id": me.get("accountId") or me.get("name"), "name": me.get("displayName", "")}

    def issue(self, key: str) -> dict:
        data = self._call("GET", f"/rest/api/2/issue/{key}",
                          params={"fields": "summary,status,issuetype,assignee,description,priority,comment,labels"})
        f = data["fields"]
        assignee = f.get("assignee") or {}
        return {
            "key": data["key"],
            "summary": f.get("summary", ""),
            "status": (f.get("status") or {}).get("name", ""),
            "type": (f.get("issuetype") or {}).get("name", ""),
            "priority": (f.get("priority") or {}).get("name", ""),
            "assignee_id": assignee.get("accountId") or assignee.get("name"),
            "assignee": assignee.get("displayName", ""),
            "description": f.get("description") or "",
            "labels": f.get("labels") or [],
            "comments": [c.get("body", "") for c in (f.get("comment") or {}).get("comments", [])
                         if isinstance(c.get("body"), str)],
        }

    def search(self, jql: str, limit: int = 50) -> list:
        fields = "summary,status,issuetype,assignee,priority"
        if self.cloud:
            data = self._call("GET", "/rest/api/3/search/jql", params={"jql": jql, "maxResults": limit, "fields": fields})
        else:
            data = self._call("GET", "/rest/api/2/search", params={"jql": jql, "maxResults": limit, "fields": fields})
        rows = []
        for item in data.get("issues", []):
            f = item["fields"]
            rows.append({"key": item["key"], "summary": f.get("summary", ""),
                         "status": (f.get("status") or {}).get("name", ""),
                         "type": (f.get("issuetype") or {}).get("name", ""),
                         "assignee": (f.get("assignee") or {}).get("displayName", "")})
        return rows

    def transitions(self, key: str) -> list:
        data = self._call("GET", f"/rest/api/2/issue/{key}/transitions")
        return [(t["id"], t["to"]["name"]) for t in data.get("transitions", [])]

    def transition(self, key: str, status: str) -> None:
        """Переводит задачу в статус. Ищет переход по имени целевого статуса."""
        available = self.transitions(key)
        match = [tid for tid, name in available if name.lower() == status.lower()]
        if not match:
            names = ", ".join(sorted({n for _, n in available})) or "нет"
            raise ApiError(f"Ошибка Jira: из текущего статуса {key} нет перехода в «{status}». "
                           f"Доступно: {names}. Проверь jira.status в config.json или workflow Jira.")
        self._call("POST", f"/rest/api/2/issue/{key}/transitions", {"transition": {"id": match[0]}})

    def assign(self, key: str, user_id) -> None:
        """Назначает исполнителя. user_id=None снимает исполнителя."""
        body = {"accountId": user_id} if self.cloud else {"name": user_id}
        self._call("PUT", f"/rest/api/2/issue/{key}/assignee", body)

    def add_labels(self, key: str, labels: list) -> None:
        self._call("PUT", f"/rest/api/2/issue/{key}", {"update": {"labels": [{"add": label} for label in labels]}})

    def comment(self, key: str, text: str) -> None:
        self._call("POST", f"/rest/api/2/issue/{key}/comment", {"body": text})


# ---------- GitLab ----------

def project_path(repo_url: str) -> str:
    """https://host/group/sub/repo.git → group/sub/repo."""
    from _wiki import normalize_repo
    return normalize_repo(repo_url).split("/", 1)[1]


class GitLab:
    def __init__(self, cfg: dict):
        self.url = cfg["url"].rstrip("/")
        self.headers = {"PRIVATE-TOKEN": secret("gitlab.token")}

    def _call(self, method, path, body=None, params=None):
        url = f"{self.url}/api/v4{path}" + (f"?{urllib.parse.urlencode(params)}" if params else "")
        return _request(method, url, self.headers, body, "GitLab")

    @staticmethod
    def _pid(project: str) -> str:
        return urllib.parse.quote(project, safe="")

    def user(self) -> dict:
        me = self._call("GET", "/user")
        return {"id": me["id"], "username": me["username"], "name": me.get("name", "")}

    def in_group(self, group: str, user_id: int) -> bool:
        try:
            self._call("GET", f"/groups/{self._pid(group)}/members/all/{user_id}")
        except ApiError as exc:
            if "404" in str(exc):
                return False
            raise
        return True

    def find_mr(self, project: str, branch: str):
        """Последний MR из ветки branch или None."""
        items = self._call("GET", f"/projects/{self._pid(project)}/merge_requests",
                           params={"source_branch": branch, "state": "all", "order_by": "created_at"})
        return items[0] if items else None

    def user_ids(self, usernames) -> list:
        """ID пользователей GitLab по логинам. Неизвестный логин — ошибка: ревьюер не должен потеряться молча."""
        ids = []
        for name in dict.fromkeys(usernames):
            found = self._call("GET", "/users", params={"username": name})
            if not found:
                raise ApiError(f"Ошибка GitLab: пользователь «{name}» не найден. Проверь reviewers в реестре или config.")
            ids.append(found[0]["id"])
        return ids

    def token_expires(self):
        """Дата окончания текущего Personal Access Token (ГГГГ-ММ-ДД) или None."""
        return self._call("GET", "/personal_access_tokens/self").get("expires_at")

    def create_mr(self, project: str, branch: str, target: str, title: str, description: str, reviewers=()) -> dict:
        return self._call("POST", f"/projects/{self._pid(project)}/merge_requests", {
            "source_branch": branch, "target_branch": target, "title": title,
            "description": description, "remove_source_branch": True, "reviewer_ids": list(reviewers),
        })

    def update_mr(self, project: str, iid: int, title: str, description: str, reviewers=()) -> dict:
        body = {"title": title, "description": description}
        if reviewers:
            body["reviewer_ids"] = list(reviewers)
        return self._call("PUT", f"/projects/{self._pid(project)}/merge_requests/{iid}", body)

    def upsert_mr(self, project, branch, target, title, description, reviewers=()) -> dict:
        """Создаёт MR или обновляет открытый MR этой ветки. reviewers — ID пользователей."""
        mr = self.find_mr(project, branch)
        if mr and mr["state"] == "opened":
            return self.update_mr(project, mr["iid"], title, description, reviewers)
        return self.create_mr(project, branch, target, title, description, reviewers)

    def approved(self, project: str, iid: int) -> bool:
        data = self._call("GET", f"/projects/{self._pid(project)}/merge_requests/{iid}/approvals")
        return bool(data.get("approved")) and bool(data.get("approved_by"))
