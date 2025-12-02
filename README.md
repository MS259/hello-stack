# Hello Stack

Small demo project to test a modern Python backend stack:

- Python + FastAPI
- Pytest
- Virtual environment (.venv)
- Git + GitHub
- GitHub Actions (CI)

## How to run

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1  # or activate.bat
pip install -r requirements.txt
uvicorn app.main:app --reload
