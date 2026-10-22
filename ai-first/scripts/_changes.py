"""Страница изменения wiki/changes/<KEY>.md: цель, критерии, требования и сценарии, MR.

Страницу создаёт только changes_sync.py в CI wiki-репозитория. Люди и агенты её не пишут.
Это модуль, а не скил: префикс «_» исключает его из проверки check_skills.py.
"""
from _flow import (find_change, find_intent, git, intent_files, intents_rel, is_none, parse_intent, parse_tasks,
                   sections, show_file)
from _tracker import project_path
from _wiki import frontmatter, today


def spec_branch(key: str) -> str:
    return f"change/{key}"


def code_branch(cfg: dict, issue: dict, change: str) -> str:
    prefix = cfg["jira"].get("branch_prefix", {}).get(issue["type"], "feature")
    slug = change.split("-", 2)[-1]  # mk8s-101-incremental-backup → incremental-backup
    return f"{prefix}/{issue['key']}-{slug}"


def requirements(ms, ref: str, change: str) -> list:
    """[(capability, операция, требование, [сценарии])] из delta-спек change на ref."""
    rows = []
    folder = f"openspec/changes/{change}/specs"
    for path in git(ms, "ls-tree", "-r", "--name-only", ref, "--", folder).splitlines():
        capability = path[len(folder) + 1:].rsplit("/", 1)[0]
        for op, body in sections(show_file(ms, ref, path) or "").items():
            for req, req_body in sections(body, 3).items():
                if req.startswith("Requirement:"):
                    scenarios = [s.removeprefix("Scenario:").strip()
                                 for s in sections(req_body, 4) if s.startswith("Scenario:")]
                    rows.append((capability, op.replace(" Requirements", ""),
                                 req.removeprefix("Requirement:").strip(), scenarios))
    return rows


def merge_requests(cfg, registry, gitlab, ms, ref, issue, change) -> dict:
    """{репозиторий: MR}: MR спецификации и MR кода каждого компонента из tasks.md."""
    found = {}
    spec = gitlab.find_mr(cfg["master_spec"]["project"], spec_branch(issue["key"]))
    if spec:
        found["master-spec"] = spec
    tasks = parse_tasks(show_file(ms, ref, f"openspec/changes/{change}/tasks.md") or "")
    branch = code_branch(cfg, issue, change)
    for name in tasks:
        entry = registry["components"].get(name) or registry["modules"].get(name)
        if entry and (mr := gitlab.find_mr(project_path(entry["repo"]), branch)):
            found[name] = mr
    return found


def page(cfg, registry, jira, gitlab, ms, key: str):
    """Текст страницы или (None, причина), если спецификация ещё не влита в main."""
    ref = f"origin/{cfg['gitlab']['default_branch']}"
    change = find_change(ms, key, ref)
    intent_name = find_intent(ms, cfg, key, ref)
    if not change or not intent_name:
        return None, f"{key}: intent или change ещё не влиты в {ref}"
    issue = jira.issue(key)
    intent = parse_intent(intent_files(ms, cfg, intent_name, ref)[0] or "")
    reqs = requirements(ms, ref, change)
    mrs = merge_requests(cfg, registry, gitlab, ms, ref, issue, change)
    intents = intents_rel(cfg)
    lines = [frontmatter(title=f"{key}: {issue['summary']}", type="change", components=intent["components"],
                         jira=jira.browse(key), change=f"openspec/changes/{change}", intent=f"{intents}/{change}",
                         status=issue["status"], updated=today(), generated="true"),
             f"# {key}: {issue['summary']}\n",
             f"Задача: [{key}]({jira.browse(key)}) · статус Jira: {issue['status']} · master-spec: "
             f"`openspec/changes/{change}/`, `{intents}/{change}/`\n",
             "## Цель\n", intent["sections"].get("Цель", ""), "",
             "## Критерии приёмки\n", *[f"{i}. {c}" for i, c in enumerate(intent["criteria"], 1)], "",
             "## Требования и сценарии\n"]
    if not reqs:
        lines.append("Изменение не меняет поведение (skip_specs).\n")
    for capability, op, req, scenarios in reqs:
        lines.append(f"### {capability}: {req}\n\n{op}. Сценарии: " + ("; ".join(scenarios) or "—") + "\n")
    lines += ["## Merge requests\n", "| Репозиторий | MR | Состояние |", "|-------------|----|-----------|"]
    lines += [f"| {name} | [!{mr['iid']}]({mr['web_url']}) | {mr['state']} |" for name, mr in mrs.items()]
    impact = intent["impact"]
    lines += ["", "## Влияние на L2/L3\n", "Нет." if is_none(impact) else impact]
    return "\n".join(lines).rstrip() + "\n", None
