# 🚀 AI Document Reader - Startup Guide

## ✅ Quick Start (Recommended)

### **Windows Users:**
```bash
# Double-click or run:
start.bat
```

### **All Platforms:**
```bash
npm run dev
```

## 📋 Available Commands

### **Development Commands**
```bash
npm run dev              # Start all services in development mode
npm run server           # Start backend only (with nodemon)
npm run client           # Start frontend only (Vite dev server)
npm run ai-service       # Start AI service only (with reload)
```

### **Production Commands**
```bash
npm run build            # Build frontend for production
npm run start            # Start all services in production mode
npm run start:server     # Start backend (production)
npm run start:client     # Start frontend preview (production)
npm run start:ai         # Start AI service (production)
```

### **Utility Commands**
```bash
npm run install-all      # Install all dependencies
npm run clean            # Clean build files and node_modules
```

## 🎯 What Each Command Does

### **`npm run dev`** (Development)
Starts all three services simultaneously:
- **Frontend**: http://localhost:3000 (Vite dev server with HMR)
- **Backend**: http://localhost:5002 (Express with nodemon)
- **AI Service**: http://localhost:8001 (FastAPI with auto-reload)

**Features:**
- ✅ Hot Module Replacement (HMR)
- ✅ Auto-restart on file changes
- ✅ Source maps for debugging
- ✅ Fast refresh

### **`npm run start`** (Production)
Starts all services in production mode:
- **Application**: http://localhost:5002 (Backend serves frontend)
- **Backend API**: http://localhost:5002/api
- **AI Service**: http://localhost:8001

**Features:**
- ✅ Optimized builds
- ✅ Minified assets
- ✅ Production-ready
- ✅ Single port access

## 🔧 Service Details

### **Frontend (React + Vite)**
- **Dev Port**: 3000
- **Prod Port**: Served by backend on 5002
- **Tech**: React, Tailwind CSS, Framer Motion
- **Build Output**: `frontend/dist/`

### **Backend (Node.js + Express)**
- **Port**: 5002
- **Tech**: Express, Multer, Axios
- **Endpoints**: `/api/upload`, `/api/get-content`, `/api/generate-audio`

### **AI Service (Python + FastAPI)**
- **Port**: 8001
- **Tech**: FastAPI, PyPDF2, gTTS, python-docx
- **Features**: Code analysis, document processing, audio generation

## 📁 Directory Structure

```
ai-document-reader/
├── frontend/              # React frontend
│   ├── src/              # Source files
│   ├── dist/             # Production build (after npm run build)
│   └── package.json
├── backend/              # Node.js backend
│   ├── server.js         # Main server file
│   └── uploads/          # File uploads directory
├── ai-service/           # Python AI service
│   ├── main.py           # FastAPI application
│   ├── audio/            # Generated audio files
│   └── requirements.txt
├── start.bat             # Windows startup script
├── start-production.bat  # Windows production script
└── package.json          # Root package.json
```

## 🐛 Troubleshooting

### **Port Already in Use**
```bash
# Windows
netstat -ano | findstr :3000
netstat -ano | findstr :5002
netstat -ano | findstr :8001
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:3000 | xargs kill -9
lsof -ti:5002 | xargs kill -9
lsof -ti:8001 | xargs kill -9
```

### **Dependencies Not Found**
```bash
# Reinstall all dependencies
npm run clean
npm run install-all
```

### **Python Dependencies Missing**
```bash
cd ai-service
pip install -r requirements.txt
```

### **Build Fails**
```bash
# Clean and rebuild
npm run clean
cd frontend
npm install
npm run build
```

## 🎯 First Time Setup

### **Step 1: Install Dependencies**
```bash
npm run install-all
```

This will:
- Install root dependencies
- Install frontend dependencies
- Install Python dependencies

### **Step 2: Verify Installation**
```bash
# Check Node.js
node --version  # Should be v16+

# Check Python
python --version  # Should be v3.8+

# Check npm
npm --version
```

### **Step 3: Start Application**
```bash
# Development
npm run dev

# Or use Windows batch file
start.bat
```

## 🚀 Production Deployment

### **Step 1: Build Frontend**
```bash
npm run build
```

### **Step 2: Set Environment**
```bash
# Windows
set NODE_ENV=production

# Linux/Mac
export NODE_ENV=production
```

### **Step 3: Start Services**
```bash
npm run start

# Or use Windows batch file
start-production.bat
```

## 📊 Service Status Check

### **Check if Services are Running**
```bash
# Frontend (dev)
curl http://localhost:3000

# Backend
curl http://localhost:5002/api/health

# AI Service
curl http://localhost:8001/
```

### **Expected Responses**
- **Frontend**: HTML page
- **Backend**: `{"status":"healthy",...}`
- **AI Service**: `{"message":"🤖 AI Document Reader Service is running!","status":"active"}`

## 🎉 Success Indicators

When all services start successfully, you should see:

```
🚀 Backend API Server running on port 5002
📁 File uploads: http://localhost:5002/uploads
🔗 API endpoints: http://localhost:5002/api
💡 Ready for AI integration!

INFO: Uvicorn running on http://127.0.0.1:8001
INFO: Application startup complete.

VITE v4.5.14  ready in 454 ms
➜  Local:   http://localhost:3000/
```

## 🔄 Restart Services

### **Development Mode**
```bash
# Press Ctrl+C to stop
# Then run again:
npm run dev
```

### **Production Mode**
```bash
# Press Ctrl+C to stop
# Then run again:
npm run start
```

## 💡 Tips

1. **Use Development Mode** for coding and testing
2. **Use Production Mode** for deployment and demos
3. **Check logs** if services don't start
4. **Ensure ports are free** before starting
5. **Keep dependencies updated** regularly

## 🎯 Quick Reference

| Command | Purpose | Ports |
|---------|---------|-------|
| `npm run dev` | Development | 3000, 5002, 8001 |
| `npm run start` | Production | 5002, 8001 |
| `start.bat` | Windows Dev | 3000, 5002, 8001 |
| `start-production.bat` | Windows Prod | 5002, 8001 |

---

**Your AI Document Reader is ready to use! 🚀**