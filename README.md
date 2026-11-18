# TugasGerald

A Tkinter project created for uprak PBGTM

## Requirements

- **Git**
- **uv** (Python package and project manager): https://docs.astral.sh/uv/
- **Python 3.12+**. You don't need to install it yourself, because uv downloads it automatically thanks to LovelyZ UwU.

No `pip install` is needed. The project has no third-party dependencies, and `tkinter` is part of Python's standard library.

## Setup

### 1. Install uv

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen your terminal afterwards, then check that it works:
```bash
uv --version
```

### 2. Clone the project

```bash
git clone <your-repo-url>
cd TugasGerald
```

### 3. Run

```bash
uv run main.py
```

On the first run, uv downloads Python 3.12 if you don't have it. It then creates a `.venv` and runs the app. A window titled **My Tk App** should open.

## Troubleshooting

| Problem | Fix |
|---|---|
| `uv: command not found` | Reopen your terminal. If it still fails, make sure uv's install folder is on your PATH. On Windows that is `C:\Users\<you>\.local\bin`. |
| `ModuleNotFoundError: No module named 'tkinter'` (Linux) | Install it with your package manager: `sudo apt install python3-tk` (Debian/Ubuntu) or `sudo dnf install python3-tkinter` (Fedora). |
| `ModuleNotFoundError: No module named 'tkinter'` (macOS, Homebrew Python) | Run `brew install python-tk@3.12`. |
| `.env` errors | Copy `.env.example` to `.env`. It is currently empty, so nothing is required. |

## Project structure

```
TugasGerald/
├── main.py              # Tkinter app entry point
├── src/tugasgerald/     # Python package (placeholder)
├── pyproject.toml       # Project metadata (uv)
├── .python-version      # Python version used by uv (3.12)
└── .env.example         # Example environment variables
```
