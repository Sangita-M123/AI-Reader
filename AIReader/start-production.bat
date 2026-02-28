@echo off
echo.
echo ========================================
echo   AI Document Reader - Production
echo ========================================
echo.

REM Set production environment
set NODE_ENV=production

REM Check dependencies
if not exist "node_modules\" (
    echo [ERROR] Dependencies not found!
    echo Please run: npm run install-all
    pause
    exit /b 1
)

REM Create directories
if not exist "uploads\" mkdir uploads
if not exist "ai-service\audio\" mkdir ai-service\audio

echo [1/3] Building frontend...
call npm run build:client
if errorlevel 1 (
    echo [ERROR] Frontend build failed!
    pause
    exit /b 1
)

echo.
echo [2/3] Frontend build complete!
echo.
echo [3/3] Starting production services...
echo.
echo Application: http://localhost:5002
echo Backend API: http://localhost:5002/api
echo AI Service: http://localhost:8001
echo.
echo Press Ctrl+C to stop all services
echo.

REM Start production services
npm run start

pause