# testme

A playground for GitHub Actions. The app is a tiny Python greeter. The point of the repo is the pipeline.

## What runs when

| Event | Workflow | Jobs |
|---|---|---|
| PR opened / title edited / new commits | `pr-title.yml` | **PR title**: the title must start with `TEST-<number>` |
| PR opened / new commits | `ci.yml` | **Lint & test** (pylint + pytest), then **Docker build** (build + smoke-run, no push) |
| Merge to `main` (or "Run workflow" button) | `cd.yml` | **Verify main**, then **Build release image** (tags `testme:<sha>` and `testme:latest`, smoke test, summary report), then **Deploy (dry run)** |

The images are never pushed anywhere. They exist only on the runner and are gone when the job finishes.

## Merge gate

`main` is protected. A PR can be merged only when these checks are green: **PR title**, **Lint & test** and **Docker build**.
Direct pushes to `main` are blocked, and the rule applies to admins too.

## Try it

```bash
git switch -c try-ci
echo "# change" >> README.md && git commit -am "change" && git push -u origin try-ci
# Open a PR titled "hello". PR title goes red and Merge stays blocked.
# Rename it to "TEST-1: hello". The check re-runs, goes green, and Merge unlocks.
```

## Run locally

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
.venv/bin/pylint app tools tests && .venv/bin/pytest
.venv/bin/python -m tools.pr_title "TEST-1: my change"
docker build -t testme . && docker run --rm testme Guy
```
