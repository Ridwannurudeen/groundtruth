# Phase 6 Results

Generated: 2026-07-03

## Gate

- README added at `README.md`.
- Required hackathon AI-use disclosure added at `AI_USAGE.md`; `docs/AI_USAGE.md` points to it.
- Demo script present at `docs/DEMO.md`.
- Screenshot asset present at `docs/screenshots/desktop-hero.png`.
- `.env.example` is present; `.env` remains gitignored and unstaged.
- No deployment, publish, push, form submission, or hackathon submission was performed.

## Final Pytest

Command:

```powershell
$env:PYTHONIOENCODING='utf-8'; .\.venv\Scripts\python.exe -m pytest -q
```

Output summary:

```text
............                                                             [100%]
12 passed, 12 warnings in 90.60s (0:01:30)
```

Warnings are from FastAPI TestClient deprecation and Cognee/Pydantic dependency deprecations already observed in earlier phases.

## Demo State

- Phase 5 live verification processed R014 through `/retract`.
- Next active demo retraction is R015.
- Local server command:

```powershell
$env:PYTHONIOENCODING='utf-8'; .\.venv\Scripts\uvicorn.exe web.app:app --host 127.0.0.1 --port 8000
```
