# 🤖 AI Document Reader

An intelligent document processing application powered by AI/ML technologies that can read, summarize, and generate audio output for various document types and code files.

## ✨ Features

- **Multi-Format Support**: PDF, Word, PowerPoint, Text, and Code files (JS, Python, Java, C++, C, C#, PHP, Ruby, Go, Rust, TypeScript, and more)
- **Advanced Universal Code Analyzer**: Deep syntax analysis for ALL programming languages
- **AI-Powered Processing**: Intelligent summarization using NLP techniques
- **Smart Code Intelligence**: Understands code structure, algorithms, data structures, and programming concepts
- **Language-Specific Analysis**: Detects and explains language-specific features and syntax
- **Advanced Audio Features**: 
  - Text-to-speech conversion with 12 speed options (0.25x to 3x)
  - Audio download functionality
  - Interactive progress bar with seek functionality
  - Real-time playback controls
- **Interactive UI**: Modern, responsive design with smooth animations
- **Real-time Processing**: Fast document analysis and content extraction

## 🛠️ Tech Stack

### Frontend
- **React.js** - Modern UI library
- **Vite** - Fast build tool and dev server
- **Tailwind CSS** - Utility-first styling
- **Framer Motion** - Smooth animations
- **React Dropzone** - File upload handling
- **Axios** - HTTP client

### Backend
- **Node.js + Express** - API server
- **Multer** - File upload handling
- **Axios** - HTTP requests to AI service

### AI/ML Service
- **Python FastAPI** - High-performance AI service
- **PyPDF2** - PDF processing
- **python-docx** - Word document handling
- **python-pptx** - PowerPoint processing
- **gTTS** - Google Text-to-Speech
- **NLP Algorithms** - Content summarization

## 🚀 Quick Start

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- npm or yarn

### 🎯 Super Easy Setup (Windows)

**One-Click Start:**
```bash
# 1. Install all dependencies (first time only)
npm run install-all

# 2. Start the application
start.bat
```

**Or for Production:**
```bash
start-production.bat
```

### 🎯 Cross-Platform Setup

**Development Mode:**
```bash
# Install dependencies
npm run install-all

# Start all services
npm run dev
```

**Production Mode:**
```bash
# Install dependencies
npm run install-all

# Build and start
npm run build
set NODE_ENV=production  # Windows
# export NODE_ENV=production  # Linux/Mac
npm run start
```

**Option 3: Manual Setup (if needed)**

1. **Install Backend Dependencies**
   ```bash
   npm install
   ```

2. **Install Frontend Dependencies**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

3. **Install AI Service Dependencies**
   ```bash
   cd ai-service
   pip install -r requirements.txt
   cd ..
   ```

4. **Start All Services**
   ```bash
   npm run dev
   ```

### Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5001
- **AI Service**: http://localhost:8001

## 📁 Project Structure

```
ai-document-reader/
├── frontend/              # React.js frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   │   ├── Header.jsx
│   │   │   ├── FileUpload.jsx
│   │   │   └── ContentDisplay.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
├── backend/               # Node.js API server
│   ├── server.js
│   └── uploads/           # File uploads directory
├── ai-service/            # Python FastAPI service
│   ├── main.py
│   ├── requirements.txt
│   └── audio/             # Generated audio files
├── package.json
└── README.md
```

## 🔧 API Endpoints

### Backend (Node.js) - Port 5001
- `POST /api/upload` - Upload and process files
- `POST /api/get-content` - Get full content or summary
- `POST /api/generate-audio` - Generate audio from text

### AI Service (Python) - Port 8001
- `GET /` - Health check
- `POST /process-file` - Extract and analyze file content
- `POST /get-content` - Process content based on type
- `POST /generate-audio` - Text-to-speech conversion

## 🎯 How to Use

1. **Upload a File**
   - Drag and drop or click to browse
   - Supports: PDF, DOCX, PPTX, TXT, JS, PY, JAVA, CPP, C

2. **Choose Content Type**
   - For documents: Full content or AI summary
   - For code: Code explanation (not code reading)

3. **Generate Audio**
   - Click "Generate Audio" button
   - Listen to the processed content

4. **Interactive Playback**
   - Play/pause audio controls
   - Reset to upload new file

## 🧠 AI Features

- **Document Summarization**: Extracts key information from long documents
- **Code Explanation**: Converts code logic into plain English explanations
- **Content Classification**: Automatically detects file types and content
- **Audio Generation**: High-quality text-to-speech output

## 📝 Resume-Ready Technologies

This project demonstrates proficiency in:
- ⚛️ Modern Frontend Development (React, Vite, Tailwind)
- 🎨 Advanced UI/UX Design (Animations, Responsive Design)
- 🚀 Backend API Development (Node.js, Express)
- 🤖 AI/ML Integration (Python, FastAPI, NLP)
- 📁 File Processing (Multiple formats)
- 🔊 Audio Generation (Text-to-Speech)
- 🔄 Full-Stack Integration
- 📦 Modern Build Tools (Vite, npm)

## 🔮 Future Enhancements

- Integration with advanced LLM models (GPT-4, Claude)
- Multi-language support for audio
- Batch file processing
- User authentication and file history
- Advanced code analysis with syntax highlighting
- Custom AI model training
- Database integration for file storage
- Cloud deployment (AWS, Azure, GCP)

## 📄 License

MIT License

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

---

**Built with ❤️ using modern AI/ML technologies**
