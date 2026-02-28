import React, { useState } from 'react';
import { motion } from 'framer-motion';
import FileUpload from './components/FileUpload';
import ContentDisplay from './components/ContentDisplay';
import Header from './components/Header';

function App() {
  const [uploadedFile, setUploadedFile] = useState(null);
  const [fileData, setFileData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileUpload = (file, data) => {
    setUploadedFile(file);
    setFileData(data);
  };

  const handleReset = () => {
    setUploadedFile(null);
    setFileData(null);
  };

  return (
    <div className="min-h-screen gradient-bg">
      <Header />
      
      <main className="container mx-auto px-4 py-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="max-w-4xl mx-auto"
        >
          {!uploadedFile ? (
            <FileUpload 
              onFileUpload={handleFileUpload}
              loading={loading}
              setLoading={setLoading}
            />
          ) : (
            <ContentDisplay 
              file={uploadedFile}
              fileData={fileData}
              onReset={handleReset}
            />
          )}
        </motion.div>
      </main>
    </div>
  );
}

export default App;