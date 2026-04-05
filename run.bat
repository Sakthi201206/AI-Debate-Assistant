@echo off
echo ============================================
echo    AI Debate Assistant — Starting Up
echo ============================================
echo.

:: Start FastAPI backend
echo [1/2] Starting FastAPI backend on http://localhost:8000 ...
start "AI Debate Backend" cmd /k "cd /d "%~dp0" && python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload"

:: Wait 3 seconds for backend to initialise (FAISS index)
timeout /t 3 /nobreak >nul

:: Start Vite frontend
echo [2/2] Starting React frontend on http://localhost:5173 ...
start "AI Debate Frontend" cmd /k "cd /d "%~dp0frontend" && npm run dev"

echo.
echo ============================================
echo  Backend  →  http://localhost:8000
echo  Frontend →  http://localhost:5173
echo  API Docs →  http://localhost:8000/docs
echo ============================================
echo.
echo Note: First run may take ~30s to build the FAISS index.
echo Press any key to exit this window (servers keep running).
pause >nul
