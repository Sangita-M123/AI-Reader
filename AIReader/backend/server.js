const express = require('express');
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const axios = require('axios');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5002;

// Middleware
app.use(cors());
app.use(express.json());
app.use('/uploads', express.static('uploads'));

// Serve static files from frontend build (for production)
if (process.env.NODE_ENV === 'production') {
  app.use(express.static(path.join(__dirname, '../frontend/dist')));
}

// Create uploads directory if it doesn't exist
if (!fs.existsSync('uploads')) {
  fs.mkdirSync('uploads');
}

// File upload configuration
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, file.fieldname + '-' + uniqueSuffix + path.extname(file.originalname));
  }
});

const upload = multer({ 
  storage: storage,
  fileFilter: (req, file, cb) => {
    const allowedTypes = ['.pdf', '.docx', '.doc', '.pptx', '.txt', '.js', '.py', '.java', '.cpp', '.c'];
    const fileExt = path.extname(file.originalname).toLowerCase();
    if (allowedTypes.includes(fileExt)) {
      cb(null, true);
    } else {
      cb(new Error('File type not supported'), false);
    }
  }
});

// Routes
app.get('/', (req, res) => {
  res.json({ 
    message: 'AI Document Reader API is running!',
    version: '1.0.0',
    endpoints: ['/api/upload', '/api/get-content', '/api/generate-audio']
  });
});

// File upload endpoint
app.post('/api/upload', upload.single('file'), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }

    console.log('File uploaded:', req.file.originalname);

    const fileInfo = {
      filename: req.file.filename,
      originalName: req.file.originalname,
      size: req.file.size,
      mimetype: req.file.mimetype,
      path: req.file.path
    };

    // Send file to AI service for processing
    try {
      const absolutePath = path.resolve(req.file.path);
      console.log('Sending to AI service:', absolutePath);
      
      const aiResponse = await axios.post('http://localhost:8001/process-file', {
        filePath: absolutePath,
        fileName: req.file.originalname,
        fileType: path.extname(req.file.originalname).toLowerCase()
      });

      console.log('AI processing successful');

      res.json({
        success: true,
        file: fileInfo,
        aiData: aiResponse.data
      });
    } catch (aiError) {
      console.error('AI service error:', aiError.message);
      // Fallback to basic response if AI service fails
      res.json({
        success: true,
        file: fileInfo,
        aiData: {
          contentType: path.extname(req.file.originalname).toLowerCase() === '.js' || 
                       path.extname(req.file.originalname).toLowerCase() === '.py' ? 'code' : 'document',
          fileType: path.extname(req.file.originalname).toLowerCase(),
          contentLength: req.file.size,
          preview: 'File uploaded successfully'
        }
      });
    }

  } catch (error) {
    console.error('Upload error:', error);
    res.status(500).json({ error: 'File processing failed' });
  }
});

// Get content endpoint
app.post('/api/get-content', async (req, res) => {
  try {
    const { filePath, contentType } = req.body;
    
    console.log('Getting content:', contentType, 'for file:', filePath);

    // Call AI service to get content
    try {
      const absolutePath = path.resolve(filePath);
      console.log('Getting content from:', absolutePath);
      
      const response = await axios.post('http://localhost:8001/get-content', {
        filePath: absolutePath,
        contentType
      });

      console.log('Content retrieved successfully');

      res.json(response.data);
    } catch (aiError) {
      console.error('AI service error:', aiError.message);
      res.status(500).json({ error: 'Failed to process content with AI service' });
    }
  } catch (error) {
    console.error('Content retrieval error:', error);
    res.status(500).json({ error: 'Failed to get content' });
  }
});

// Generate audio endpoint
app.post('/api/generate-audio', async (req, res) => {
  try {
    const { text, language = 'en' } = req.body;
    
    console.log('Generating audio for text length:', text.length);

    // Call AI service to generate audio
    try {
      const response = await axios.post('http://localhost:8001/generate-audio', {
        text,
        language
      });

      console.log('Audio generated successfully');

      res.json(response.data);
    } catch (aiError) {
      console.error('AI service error:', aiError.message);
      res.status(500).json({ error: 'Failed to generate audio with AI service' });
    }
  } catch (error) {
    console.error('Audio generation error:', error);
    res.status(500).json({ error: 'Failed to generate audio' });
  }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

// Catch-all handler for production (serve React app)
if (process.env.NODE_ENV === 'production') {
  app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../frontend/dist/index.html'));
  });
}

app.listen(PORT, () => {
  console.log(`🚀 Backend API Server running on port ${PORT}`);
  console.log(`📁 File uploads: http://localhost:${PORT}/uploads`);
  console.log(`🔗 API endpoints: http://localhost:${PORT}/api`);
  console.log(`💡 Ready for AI integration!`);
  
  if (process.env.NODE_ENV === 'production') {
    console.log(`🌐 Frontend served at: http://localhost:${PORT}`);
  }
});