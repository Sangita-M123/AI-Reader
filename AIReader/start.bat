@echo off
echo.
echo ========================================
echo   AI Document Reader - Starting...
echo ========================================
echo.

REM Check if node_modules exists
if not exist "node_modules\" (
    echo [ERROR] Dependencies not found!
    echo Please run: npm run install-all
    pause
    exit /b 1
)

REM Check if frontend/node_modules exists
if not exist "frontend\node_modules\" (
    echo [ERROR] Frontend dependencies not found!
    echo Please run: npm run install-all
    pause
    exit /b 1
)

REM Create necessary directories
if not exist "uploads\" mkdir uploads
if not exist "ai-service\audio\" mkdir ai-service\audio

echo [OK] All dependencies found!
echo.
echo Starting services...
echo.
echo Frontend: http://localhost:3000
echo Backend:  http://localhost:5002
echo AI Service: http://localhost:8001
echo.
echo Press Ctrl+C to stop all services
echo.

REM Start all services using npm
npm run dev

pause