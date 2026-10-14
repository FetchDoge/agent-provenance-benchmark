#!/usr/bin/env python3
"""Framework candidate enumeration for the Provenance Benchmark pre-reg packet.

Method (frozen in the packet, per rubric v14 §4):
  GitHub search `topic:ai-agents stars:>=1000` (sorted by stars desc, all pages)
  UNION repos linked from two awesome-lists at frozen commits:
    - e2b-dev/awesome-ai-agents
    - slavakurilyak/awesome-ai-agents

Output: raw JSON candidate list on stdout; run metadata on stderr.
The universe predicate, ranking, and SHA pinning are applied afterwards
(see FRAMEWORKS.md) — this script only enumerates.

Requires: ~/workspace/skills/github/bin/gh-api.py (custom.github credential).
"""
import json
import re
import subprocess
import sys
from datetime import datetime, timezone

GH_API = "/home/hatch/workspace/skills/github/bin/gh-api.py"
AWESOME = ["e2b-dev/awesome-ai-agents", "slavakurilyak/awesome-ai-agents"]
REPO_LINK = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")


def gh(method, path):
    out = subprocess.run(
        ["python3", GH_API, method, path],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


def main():
    enumeration_started_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    candidates = {}  # full_name -> record

    # 1. Topic search, all pages.
    page = 1
    while True:
        d = gh("GET", f"/search/repositories?q=topic:ai-agents+stars:%3E=1000"
                      f"&sort=stars&order=desc&per_page=100&page={page}")
        items = d.get("items", [])
        if not items:
            break
        for r in items:
            fn = r["full_name"]
            rec = candidates.setdefault(fn, {
                "full_name": fn,
                "stargazers_count": r["stargazers_count"],
                "description": r.get("description") or "",
                "topics": r.get("topics", []),
                "default_branch": r.get("default_branch"),
                "html_url": r["html_url"],
                "sources": [],
            })
            if "topic:ai-agents stars:>=1000" not in rec["sources"]:
                rec["sources"].append("topic:ai-agents stars:>=1000")
        if len(items) < 100:
            break
        page += 1

    # 2. Awesome lists at frozen commits.
    frozen = {}
    for repo in AWESOME:
        meta = gh("GET", f"/repos/{repo}")
        branch = meta["default_branch"]
        # HEAD SHA of the default branch = frozen commit.
        ref = gh("GET", f"/repos/{repo}/git/ref/heads/{branch}")
        sha = ref["object"]["sha"]
        frozen[repo] = {"commit": sha, "branch": branch,
                        "stars": meta["stargazers_count"]}
        readme = gh("GET", f"/repos/{repo}/readme?ref={sha}")
        import base64
        text = base64.b64decode(readme["content"]).decode("utf-8", "replace")
        for m in REPO_LINK.finditer(text):
            fn = m.group(1)
            if fn.lower() in (a.lower() for a in AWESOME):
                continue
            rec = candidates.setdefault(fn, {
                "full_name": fn,
                "stargazers_count": None,
                "description": "",
                "topics": [],
                "default_branch": None,
                "html_url": f"https://github.com/{fn}",
                "sources": [],
            })
            if repo not in rec["sources"]:
                rec["sources"].append(repo)

    # 3. Backfill stars/topics for awesome-only repos (best effort, one call each).
    for fn, rec in candidates.items():
        if rec["stargazers_count"] is None:
            try:
                r = gh("GET", f"/repos/{fn}")
                rec["stargazers_count"] = r.get("stargazers_count", 0)
                rec["description"] = r.get("description") or ""
                rec["topics"] = r.get("topics", [])
                rec["default_branch"] = r.get("default_branch")
            except subprocess.CalledProcessError:
                rec["stargazers_count"] = 0

    print(json.dumps({
        "enumeration_started_at": enumeration_started_at,
        "method": ("GitHub search `topic:ai-agents stars:>=1000` (sort stars desc) "
                   "UNION repos linked from e2b-dev/awesome-ai-agents and "
                   "slavakurilyak/awesome-ai-agents at frozen commits"),
        "awesome_frozen": frozen,
        "candidates": sorted(candidates.values(),
                             key=lambda r: -(r["stargazers_count"] or 0)),
    }, indent=1))
    print(f"enumeration_started_at={enumeration_started_at} candidates={len(candidates)}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
