#!/usr/bin/env python3
"""Команды разработчика: intent → change-спека → реализация агентом → MR → готово к QA.

Использование:
    python scripts/developer.py queue
    python scripts/developer.py start <KEY> [--dry-run]
    python scripts/developer.py check <KEY>
    python scripts/developer.py apply <KEY> --repo <имя|путь> [--dry-run]
    python scripts/developer.py submit <KEY> --repo <имя|путь> [--repo ...] [--dry-run]

--repo принимает имя из раздела repos в config.json, например etcd-backup.
    python scripts/developer.py done <KEY> [--dry-run]
    python scripts/developer.py reject <KEY> --reason "<причина>" [--dry-run]

Статус Jira: ready_for_dev → in_progress (start) → code_review (submit) → ready_for_qa (done).
reject возвращает задачу аналитику: → analysis.

Скил: skills/developer/SKILL.md
"""
import argparse
import sys
from pathlib import Path

from _flow import (Plan, Stop, changed_files, changes_dir, check_intent, check_key, check_locked_meta,
                   check_ownership, check_spec, component_by_repo, current_branch, ensure_labels, find_change,
                   find_intent, first_line, foreign_changes, gate, git, intent_files, intents_rel, is_clean,
                   is_none, load_all, master_spec, openspec, parse_intent, parse_tasks, require_fresh, require_role,
                   resolve_repo, reviewers,
                   show_file, switch_branch)
from _changes import code_branch, merge_requests, spec_branch
from _scan import scan
from _tracker import GitLab, Jira, project_path

ROLE = "developer"


def context(args):
    cfg, registry = load_all()
    jira, gitlab = Jira(cfg["jira"]), GitLab(cfg["gitlab"])
    require_role(ROLE, cfg, gitlab)
    require_fresh(cfg)
    key = check_key(args.key) if getattr(args, "key", None) else None
    return cfg, registry, jira, gitlab, key


def require_mine(issue, me, expected, errors):
    if issue["status"] not in expected:
        errors.append(f"{issue['key']} в статусе «{issue['status']}», ожидается «{' или '.join(expected)}»")
    if issue["assignee_id"] != me["id"]:
        errors.append(f"{issue['key']} назначена не на тебя ({issue['assignee'] or 'нет исполнителя'})")


def local_spec(cfg, registry, ms, key):
    """Проверка change-спеки в рабочей копии master-spec: (change, ошибки, предупреждения, задачи)."""
    base = f"origin/{cfg['gitlab']['default_branch']}"
    errors = []
    if current_branch(ms) != spec_branch(key):
        errors.append(f"master-spec не на ветке {spec_branch(key)}. Запусти: developer.py start {key}")
    change = find_change(ms, key)
    if not change:
        return None, errors + [f"нет OpenSpec change для {key}. Запусти: developer.py start {key}"], [], {}
    errors += check_ownership(changed_files(ms, base), ROLE, cfg, change)
    errors += check_locked_meta(ms, base, change, key, cfg)
    spec_errors, warnings, tasks = check_spec(ms, change, key, cfg, registry)
    return change, errors + spec_errors, warnings, tasks


# ---------- Команды ----------

def cmd_queue(args):
    cfg, _, jira, _, _ = context(args)
    rows = jira.search(cfg["jira"]["dev_queue_jql"])
    print("Задач, готовых к разработке, нет." if not rows else "")
    for row in rows:
        print(f"{row['key']:12s} {row['assignee'] or '—':20s} {row['summary']}")
    return 0


def cmd_start(args):
    cfg, registry, jira, _, key = context(args)
    ms = master_spec(cfg)
    base = cfg["gitlab"]["default_branch"]
    st = cfg["jira"]["status"]
    issue, me = jira.issue(key), jira.myself()
    git(ms, "fetch", "-q", "origin")
    change = find_intent(ms, cfg, key, f"origin/{base}")

    errors = []
    if issue["status"] != st["ready_for_dev"]:
        errors.append(f"{key} в статусе «{issue['status']}». Брать в работу можно только из «{st['ready_for_dev']}»")
    if issue["assignee_id"] not in (None, me["id"]):
        errors.append(f"{key} назначена на {issue['assignee']}")
    if not change:
        errors.append(f"для {key} нет intent в master-spec (origin/{base}:{intents_rel(cfg)}/). Задача не готова к разработке.")
    else:
        intent, discovery = intent_files(ms, cfg, change, f"origin/{base}")
        errors += [f"intent не прошёл проверку: {e}" for e in check_intent(intent, key, registry, discovery)]
    foreign = foreign_changes(ms, f"openspec/changes/{key.lower()}-")
    if foreign:
        errors.append(f"в master-spec незакоммиченные изменения вне задачи {key}: {', '.join(foreign[:3])}")
    gate(errors)

    plan = Plan(args.dry_run)
    ensure_labels(plan, jira, cfg, issue)
    if issue["assignee_id"] != me["id"]:
        plan.add(f"Jira {key}: исполнитель — {me['name']}", lambda: jira.assign(key, me["id"]))
    plan.add(f"Jira {key}: статус → {st['in_progress']}", lambda: jira.transition(key, st["in_progress"]))
    plan.add(f"master-spec: ветка {spec_branch(key)}", lambda: switch_branch(ms, spec_branch(key), base))

    def create_change():
        if (changes_dir(ms) / change).is_dir():
            return
        result = openspec(ms, "new", "change", change, "--schema", cfg["master_spec"]["schema"])
        if "change" not in result:
            raise Stop(f"openspec new change: {result}")
        meta = changes_dir(ms) / change / ".openspec.yaml"
        meta.write_text(meta.read_text(encoding="utf-8").rstrip()
                        + f"\nx-jira: {key}\nx-intent: {intents_rel(cfg)}/{change}/intent.md\n", encoding="utf-8")
    plan.add(f"master-spec: OpenSpec change openspec/changes/{change}/ (x-jira, x-intent)", create_change)
    plan.run()

    intent = parse_intent(intent_files(ms, cfg, change, f"origin/{base}")[0])
    print(f"\nIntent: {intents_rel(cfg)}/{change}/intent.md (только чтение)")
    print(f"Discovery: {intents_rel(cfg)}/{change}/discovery.md — исследование, интервью, выбранная точка внедрения")
    print(f"Компоненты: {', '.join(intent['components'])}")
    print("Контекст wiki:")
    for name in intent["components"]:
        print(f"  python scripts/wiki_context.py -c {name}")
    print(f"\nДальше: напиши specs/, design.md, tasks.md в openspec/changes/{change}/.")
    print("Задачи в tasks.md группируй по компонентам: «## 1. <компонент>».")
    print(f"Проверь: python scripts/developer.py check {key}")
    return 0


def cmd_check(args):
    cfg, registry, jira, _, key = context(args)
    change, errors, warnings, tasks = local_spec(cfg, registry, master_spec(cfg), key)
    issue, st = jira.issue(key), cfg["jira"]["status"]
    if issue["status"] not in (st["in_progress"], st["code_review"]):
        errors.insert(0, f"{key} в статусе «{issue['status']}». Разработка идёт только в «{st['in_progress']}».")
    for w in warnings:
        print(f"ВНИМАНИЕ  {w}")
    gate(errors)
    for name, items in tasks.items():
        done = sum(1 for d, _ in items if d)
        print(f"{name}: задач {len(items)}, выполнено {done}")
    print(f"Спецификация {change} прошла проверку.")
    return 0


def check_repo(repo: Path, registry, tasks, errors):
    """Компонент репозитория или None. Ошибки добавляет в errors."""
    name = component_by_repo(repo, registry)
    if not name:
        errors.append(f"{repo}: origin не найден в wiki/code/components.toml")
    elif name not in tasks:
        errors.append(f"{repo}: компонента {name} нет в tasks.md")
    return name


def cmd_apply(args):
    cfg, registry, jira, _, key = context(args)
    ms = master_spec(cfg)
    repo = resolve_repo(args.repo)
    issue, me = jira.issue(key), jira.myself()
    errors = []
    require_mine(issue, me, [cfg["jira"]["status"]["in_progress"]], errors)
    change, spec_errors, _, tasks = local_spec(cfg, registry, ms, key)
    errors += spec_errors
    name = check_repo(repo, registry, tasks, errors) if change else None
    if not is_clean(repo):
        errors.append(f"{repo.name}: есть незакоммиченные изменения")
    gate(errors)

    branch = code_branch(cfg, issue, change)
    base = cfg["gitlab"]["default_branch"]
    plan = Plan(args.dry_run)
    plan.add(f"{repo.name}: fetch", lambda: git(repo, "fetch", "-q", "origin"))
    plan.add(f"{repo.name}: ветка {branch}", lambda: switch_branch(repo, branch, base))
    plan.run()

    folder = f"{ms}/openspec/changes/{change}"
    print(f"\nЗадание для агента. Компонент {name}, репозиторий {repo}, ветка {branch}.")
    print(f"Спецификация (читать до кода): {folder}/specs/, {folder}/design.md")
    print(f"Задачи компонента (отмечай [x] в {folder}/tasks.md после проверки):")
    for done, text in tasks[name]:
        print(f"  - [{'x' if done else ' '}] {text}")
    print(f"Контекст wiki: python scripts/wiki_context.py -c {name}")
    print(f"Код меняй только в {repo}. Intent и specs не меняй.")
    print(f"После реализации: python scripts/developer.py submit {key} --repo {repo}")
    return 0


def mr_description(jira, key, change, intent, spec_mr_url, intents):
    parts = intent["sections"]
    lines = [
        f"Задача: [{key}]({jira.browse(key)})",
        f"Спецификация: {spec_mr_url} · `openspec/changes/{change}/` · intent: `{intents}/{change}/intent.md`",
        "",
        "## Что изменено",
        parts.get("Цель", ""),
        "",
        "## Как проверить",
        *[f"{i}. {c}" for i, c in enumerate(intent["criteria"], 1)],
        "",
        "## Риски",
        parts.get("Ограничения", ""),
    ]
    if intent["impact"] and not is_none(intent["impact"]):
        lines += ["", f"Влияние на L2/L3: {first_line(intent['impact'])}"]
    return "\n".join(lines)


def cmd_submit(args):
    cfg, registry, jira, gitlab, key = context(args)
    ms = master_spec(cfg)
    base = cfg["gitlab"]["default_branch"]
    st = cfg["jira"]["status"]
    issue, me = jira.issue(key), jira.myself()
    errors = []
    require_mine(issue, me, [st["in_progress"], st["code_review"]], errors)
    change, spec_errors, _, tasks = local_spec(cfg, registry, ms, key)
    errors += spec_errors
    gate(errors)

    branch = code_branch(cfg, issue, change)
    repos = {}
    for raw in args.repo:
        repo = resolve_repo(raw)
        name = check_repo(repo, registry, tasks, errors)
        if not name:
            continue
        repos[name] = repo
        if current_branch(repo) != branch:
            errors.append(f"{repo.name}: ветка {current_branch(repo)}, ожидается {branch}")
        if not is_clean(repo):
            errors.append(f"{repo.name}: есть незакоммиченные изменения")
        if git(repo, "rev-list", "--count", f"origin/{base}..HEAD", check=False) in ("", "0"):
            errors.append(f"{repo.name}: нет коммитов относительно origin/{base}")
        open_tasks = [t for d, t in tasks.get(name, []) if not d]
        if open_tasks:
            errors.append(f"{name}: не выполнены задачи: {'; '.join(open_tasks)}")
    projects = {name: project_path(registry["components"].get(name, registry["modules"].get(name, {}))["repo"])
                for name in tasks}
    for name in tasks:
        if name not in repos and not gitlab.find_mr(projects[name], branch):
            errors.append(f"{name}: нет MR и не передан --repo. Компонент есть в tasks.md.")
    gate(errors)

    intent = parse_intent(intent_files(ms, cfg, change)[0])
    ms_project = cfg["master_spec"]["project"]
    plan = Plan(args.dry_run)
    ensure_labels(plan, jira, cfg, issue)
    if not is_clean(ms):
        plan.add(f"master-spec: коммит «{key}: спецификация изменения»", lambda: (
            git(ms, "add", f"openspec/changes/{change}"),
            git(ms, "commit", "-q", "-m", f"{key}: спецификация изменения")))
    plan.add(f"master-spec: push {spec_branch(key)}", lambda: git(ms, "push", "-q", "-u", "origin", spec_branch(key)))

    owners = {name: (registry["components"].get(name) or registry["modules"].get(name, {})).get("reviewers", [])
              for name in tasks}
    me_login = gitlab.user()["username"]

    def spec_mr():
        names = cfg.get("review", {}).get("spec_reviewers", []) + [u for n in tasks for u in owners[n]]
        plan.state["spec"] = gitlab.upsert_mr(ms_project, spec_branch(key), base, f"{key}: спецификация изменения",
                                              f"Задача: [{key}]({jira.browse(key)})\nIntent: `{intents_rel(cfg)}/{change}/intent.md`",
                                              reviewers(gitlab, names, me_login))
    plan.add(f"GitLab {ms_project}: MR {spec_branch(key)} → {base}", spec_mr)
    for name, repo in repos.items():
        plan.add(f"{name}: push {branch}", lambda repo=repo: git(repo, "push", "-q", "-u", "origin", branch))

        def code_mr(name=name):
            plan.state[name] = gitlab.upsert_mr(projects[name], branch, base, f"{key}: {issue['summary']}",
                                                mr_description(jira, key, change, intent, plan.state["spec"]["web_url"],
                                                               intents_rel(cfg)),
                                                reviewers(gitlab, owners[name], me_login))
        plan.add(f"GitLab {projects[name]}: MR {branch} → {base}", code_mr)
    if issue["status"] != st["code_review"]:
        plan.add(f"Jira {key}: статус → {st['code_review']}", lambda: jira.transition(key, st["code_review"]))
    plan.add(f"Jira {key}: комментарий со ссылками на MR", lambda: jira.comment(key, "MR на ревью:\n" + "\n".join(
        f"- {k}: {v['web_url']}" for k, v in plan.state.items())))
    plan.run()
    if not args.dry_run:
        print(f"\nПосле ревью лида и merge: python scripts/developer.py done {key}")
    return 0


def cmd_done(args):
    cfg, registry, jira, gitlab, key = context(args)
    ms = master_spec(cfg)
    base = cfg["gitlab"]["default_branch"]
    st = cfg["jira"]["status"]
    issue, me = jira.issue(key), jira.myself()
    errors = []
    require_mine(issue, me, [st["code_review"]], errors)
    git(ms, "fetch", "-q", "origin")
    change = find_change(ms, key, f"origin/{base}")
    if not change:
        errors.append(f"OpenSpec change для {key} нет в origin/{base}: MR спецификации не влит")
        gate(errors)
    mrs = merge_requests(cfg, registry, gitlab, ms, f"origin/{base}", issue, change)
    spec_mr = mrs.pop("master-spec", None)
    if not spec_mr or spec_mr["state"] != "merged":
        errors.append("MR спецификации не влит" + (f": {spec_mr['web_url']}" if spec_mr else ""))
    tasks = parse_tasks(show_file(ms, f"origin/{base}", f"openspec/changes/{change}/tasks.md") or "")
    for name in tasks:
        mr = mrs.get(name)
        if not mr:
            errors.append(f"{name}: нет MR из ветки {code_branch(cfg, issue, change)}")
            continue
        entry = registry["components"].get(name) or registry["modules"].get(name)
        if cfg["gates"]["qa_requires"] == "merged" and mr["state"] != "merged":
            errors.append(f"{name}: MR не влит: {mr['web_url']}")
        elif mr["state"] == "opened" and not gitlab.approved(project_path(entry["repo"]), mr["iid"]):
            errors.append(f"{name}: MR не одобрен: {mr['web_url']}")
        elif mr["state"] == "closed":
            errors.append(f"{name}: MR закрыт без merge: {mr['web_url']}")
    gate(errors)

    plan = Plan(args.dry_run)
    ensure_labels(plan, jira, cfg, issue)
    plan.add(f"Jira {key}: статус → {st['ready_for_qa']}", lambda: jira.transition(key, st["ready_for_qa"]))
    plan.add(f"Jira {key}: комментарий для QA", lambda: jira.comment(
        key, f"Готово к QA. Спецификация: openspec/changes/{change}/. "
             f"Страница для QA: wiki/changes/{key}.md (создаёт CI wiki после синхронизации)."))
    plan.run()
    return 0


def cmd_reject(args):
    cfg, _, jira, _, key = context(args)
    st = cfg["jira"]["status"]
    issue = jira.issue(key)
    errors = []
    if issue["status"] not in (st["ready_for_dev"], st["in_progress"]):
        errors.append(f"вернуть можно из «{st['ready_for_dev']}» или «{st['in_progress']}», сейчас «{issue['status']}»")
    if len(args.reason.strip()) < 20:
        errors.append("опиши причину конкретно: что в intent неясно или противоречиво (от 20 символов)")
    errors += [f"причина, строка {n}: похоже на {kind}" for n, kind in scan(args.reason)]
    gate(errors)
    plan = Plan(args.dry_run)
    ensure_labels(plan, jira, cfg, issue)
    plan.add(f"Jira {key}: статус → {st['analysis']}", lambda: jira.transition(key, st["analysis"]))
    plan.add(f"Jira {key}: комментарий с причиной", lambda: jira.comment(key, f"Intent возвращён на доработку: {args.reason}"))
    plan.add(f"Jira {key}: снять исполнителя — задача уходит аналитику", lambda: jira.assign(key, None))
    plan.run()
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Команды разработчика.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("queue", help="задачи, готовые к разработке")
    for name, text in (("start", "взять задачу"), ("check", "проверить change-спеку"),
                       ("apply", "подготовить репозиторий и задание агенту"), ("submit", "создать MR"),
                       ("done", "после merge: готово к QA"), ("reject", "вернуть intent аналитику")):
        p = sub.add_parser(name, help=text)
        p.add_argument("key")
        if name != "check":
            p.add_argument("--dry-run", action="store_true")
        if name == "apply":
            p.add_argument("--repo", required=True, help="имя из repos в config.json или путь к репозиторию")
        if name == "submit":
            p.add_argument("--repo", action="append", default=[], help="имя из repos в config.json или путь; можно повторять")
        if name == "reject":
            p.add_argument("--reason", required=True)
    args = parser.parse_args(argv)
    handler = {"queue": cmd_queue, "start": cmd_start, "check": cmd_check, "apply": cmd_apply,
               "submit": cmd_submit, "done": cmd_done, "reject": cmd_reject}[args.command]
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
