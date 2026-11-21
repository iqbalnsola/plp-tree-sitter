@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Venv belum ada. Jalankan dulu:
  echo   uv venv .venv
  echo   uv pip install --python .venv/Scripts/python.exe tree-sitter tree-sitter-python tree-sitter-javascript
  pause
  exit /b 1
)
".venv\Scripts\python.exe" "tugas1-3\t1.py"
echo.
pause
