import React from 'react';
import { motion } from 'framer-motion';
import { Brain, FileText, Volume2 } from 'lucide-react';

const Header = () => {
  return (
    <motion.header 
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="bg-white/10 backdrop-blur-md border-b border-white/20"
    >
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-white/20 rounded-lg">
              <Brain className="w-8 h-8 text-white" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-white">AI Document Reader</h1>
              <p className="text-white/80 text-sm">Powered by Machine Learning & NLP</p>
            </div>
          </div>
          
          <div className="flex items-center space-x-6 text-white/80">
            <div className="flex items-center space-x-2">
              <FileText className="w-5 h-5" />
              <span className="text-sm">Smart Processing</span>
            </div>
            <div className="flex items-center space-x-2">
              <Volume2 className="w-5 h-5" />
              <span className="text-sm">Audio Output</span>
            </div>
          </div>
        </div>
      </div>
    </motion.header>
  );
};

export default Header;