@echo off
cd /d "%~dp0"
if exist "runtime\python.exe" (
    "runtime\python.exe" "serve_local.py" --open
) else (
    where python >nul 2>nul
    if errorlevel 1 (
        echo Python was not found. Install Python 3 or extract the bundled runtime.
        pause
        exit /b 1
    )
    python "serve_local.py" --open
)
if errorlevel 1 (
    echo.
    echo The game server could not start. Check the error above.
    pause
)
