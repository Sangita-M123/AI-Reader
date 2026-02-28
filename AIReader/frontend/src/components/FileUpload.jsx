import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { motion } from 'framer-motion';
import { Upload, FileText, Code, Loader2 } from 'lucide-react';
import axios from 'axios';

const FileUpload = ({ onFileUpload, loading, setLoading }) => {
  const onDrop = useCallback(async (acceptedFiles) => {
    const file = acceptedFiles[0];
    if (!file) return;

    setLoading(true);
    
    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post('/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.data.success) {
        onFileUpload(file, response.data);
      }
    } catch (error) {
      console.error('Upload failed:', error);
      alert('Upload failed. Please try again.');
    } finally {
      setLoading(false);
    }
  }, [onFileUpload, setLoading]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
      'application/msword': ['.doc'],
      'application/vnd.openxmlformats-officedocument.presentationml.presentation': ['.pptx'],
      'text/plain': ['.txt'],
      'text/javascript': ['.js'],
      'text/x-python': ['.py'],
      'text/x-java-source': ['.java'],
      'text/x-c++src': ['.cpp'],
      'text/x-csrc': ['.c']
    },
    multiple: false,
    disabled: loading
  });

  const supportedFiles = [
    { icon: FileText, label: 'Documents', types: 'PDF, Word, PowerPoint, Text' },
    { icon: Code, label: 'Code Files', types: 'JavaScript, Python, Java, C++, C' }
  ];

  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="text-center text-white space-y-4"
      >
        <h2 className="text-4xl font-bold">Upload Your Document</h2>
        <p className="text-xl text-white/80 max-w-2xl mx-auto">
          Experience the power of AI-driven document analysis. Get intelligent summaries, 
          full content reading, and audio output for any document or code file.
        </p>
      </motion.div>

      {/* Upload Area */}
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5, delay: 0.2 }}
        className="glass-effect rounded-2xl p-8"
      >
        <div
          {...getRootProps()}
          className={`
            border-2 border-dashed rounded-xl p-12 text-center cursor-pointer transition-all duration-300
            ${isDragActive 
              ? 'border-blue-400 bg-blue-400/10' 
              : 'border-white/30 hover:border-white/50 hover:bg-white/5'
            }
            ${loading ? 'pointer-events-none opacity-50' : ''}
          `}
        >
          <input {...getInputProps()} />
          
          <div className="space-y-6">
            {loading ? (
              <Loader2 className="w-16 h-16 text-white mx-auto animate-spin" />
            ) : (
              <Upload className="w-16 h-16 text-white mx-auto" />
            )}
            
            <div className="space-y-2">
              <h3 className="text-2xl font-semibold text-white">
                {loading ? 'Processing...' : isDragActive ? 'Drop your file here' : 'Drag & drop your file'}
              </h3>
              <p className="text-white/70">
                {loading ? 'AI is analyzing your document' : 'or click to browse files'}
              </p>
            </div>
          </div>
        </div>

        {/* Supported Files */}
        <div className="mt-8 grid md:grid-cols-2 gap-6">
          {supportedFiles.map((fileType, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, x: index === 0 ? -20 : 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.5, delay: 0.4 + index * 0.1 }}
              className="bg-white/10 rounded-lg p-4 border border-white/20"
            >
              <div className="flex items-center space-x-3">
                <fileType.icon className="w-8 h-8 text-blue-300" />
                <div>
                  <h4 className="font-semibold text-white">{fileType.label}</h4>
                  <p className="text-sm text-white/70">{fileType.types}</p>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Features */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.6 }}
        className="grid md:grid-cols-3 gap-6"
      >
        {[
          { title: 'AI Summarization', desc: 'Get intelligent summaries using NLP' },
          { title: 'Code Explanation', desc: 'Understand code logic in plain English' },
          { title: 'Audio Output', desc: 'Listen to content with text-to-speech' }
        ].map((feature, index) => (
          <div key={index} className="glass-effect rounded-lg p-6 text-center text-white">
            <h4 className="font-semibold mb-2">{feature.title}</h4>
            <p className="text-sm text-white/70">{feature.desc}</p>
          </div>
        ))}
      </motion.div>
    </div>
  );
};

export default FileUpload;