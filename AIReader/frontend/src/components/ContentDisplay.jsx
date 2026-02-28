import React, { useState, useRef } from 'react';
import { motion } from 'framer-motion';
import { ArrowLeft, FileText, Code, Volume2, VolumeX, Loader2, Download, Settings } from 'lucide-react';
import axios from 'axios';

const ContentDisplay = ({ file, fileData, onReset }) => {
  const [contentType, setContentType] = useState('summary');
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(false);
  const [audioUrl, setAudioUrl] = useState('');
  const [audioLoading, setAudioLoading] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);
  const [playbackSpeed, setPlaybackSpeed] = useState(1);
  const [showSpeedControl, setShowSpeedControl] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const audioRef = useRef(null);

  const isCodeFile = fileData.aiData.contentType === 'code';

  const speedOptions = [
    { value: 0.25, label: '0.25x' },
    { value: 0.5, label: '0.5x' },
    { value: 0.75, label: '0.75x' },
    { value: 1, label: '1x' },
    { value: 1.25, label: '1.25x' },
    { value: 1.5, label: '1.5x' },
    { value: 1.75, label: '1.75x' },
    { value: 2, label: '2x' },
    { value: 2.25, label: '2.25x' },
    { value: 2.5, label: '2.5x' },
    { value: 2.75, label: '2.75x' },
    { value: 3, label: '3x' }
  ];

  const formatTime = (time) => {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  const handleGetContent = async (type) => {
    setLoading(true);
    setContentType(type);
    
    try {
      const response = await axios.post('/api/get-content', {
        filePath: fileData.file.path,
        contentType: type
      });

      if (response.data.success) {
        setContent(response.data.content);
      }
    } catch (error) {
      console.error('Failed to get content:', error);
      alert('Failed to get content. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateAudio = async () => {
    if (!content) {
      alert('Please load content first');
      return;
    }

    setAudioLoading(true);
    
    try {
      const response = await axios.post('/api/generate-audio', {
        text: content,
        language: 'en'
      });

      if (response.data.success) {
        setAudioUrl(response.data.audioUrl);
      }
    } catch (error) {
      console.error('Failed to generate audio:', error);
      alert('Failed to generate audio. Please try again.');
    } finally {
      setAudioLoading(false);
    }
  };

  const handleAudioPlay = () => {
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause();
        setIsPlaying(false);
      } else {
        audioRef.current.playbackRate = playbackSpeed;
        audioRef.current.play();
        setIsPlaying(true);
      }
    }
  };

  const handleSpeedChange = (speed) => {
    setPlaybackSpeed(speed);
    if (audioRef.current) {
      audioRef.current.playbackRate = speed;
    }
    setShowSpeedControl(false);
  };

  // Close speed control when clicking outside
  const handleClickOutside = (e) => {
    if (showSpeedControl && !e.target.closest('.speed-control-container')) {
      setShowSpeedControl(false);
    }
  };

  // Check if dropdown should open upward
  const [dropdownDirection, setDropdownDirection] = React.useState('down');
  
  const checkDropdownDirection = () => {
    const button = document.querySelector('.speed-control-container button');
    if (button) {
      const rect = button.getBoundingClientRect();
      const spaceBelow = window.innerHeight - rect.bottom;
      const spaceAbove = rect.top;
      
      // If less than 350px space below and more space above, open upward
      if (spaceBelow < 350 && spaceAbove > spaceBelow) {
        setDropdownDirection('up');
      } else {
        setDropdownDirection('down');
      }
    }
  };

  React.useEffect(() => {
    if (showSpeedControl) {
      checkDropdownDirection();
      document.addEventListener('click', handleClickOutside);
      return () => document.removeEventListener('click', handleClickOutside);
    }
  }, [showSpeedControl]);

  const handleDownloadAudio = () => {
    if (audioUrl) {
      const link = document.createElement('a');
      link.href = audioUrl;
      link.download = `${file.name.split('.')[0]}_audio.mp3`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  };

  const handleTimeUpdate = () => {
    if (audioRef.current) {
      setCurrentTime(audioRef.current.currentTime);
    }
  };

  const handleLoadedMetadata = () => {
    if (audioRef.current) {
      setDuration(audioRef.current.duration);
    }
  };

  const handleProgressClick = (e) => {
    if (audioRef.current && duration) {
      const rect = e.currentTarget.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const width = rect.width;
      const newTime = (clickX / width) * duration;
      audioRef.current.currentTime = newTime;
      setCurrentTime(newTime);
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-effect rounded-lg p-6"
      >
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <button
              onClick={onReset}
              className="p-2 bg-white/20 hover:bg-white/30 rounded-lg transition-colors"
            >
              <ArrowLeft className="w-5 h-5 text-white" />
            </button>
            <div className="flex items-center space-x-3">
              {isCodeFile ? (
                <Code className="w-8 h-8 text-blue-300" />
              ) : (
                <FileText className="w-8 h-8 text-blue-300" />
              )}
              <div>
                <h2 className="text-xl font-semibold text-white">{file.name}</h2>
                <p className="text-white/70 text-sm">
                  {isCodeFile ? 'Code File' : 'Document'} • {(file.size / 1024).toFixed(1)} KB
                </p>
              </div>
            </div>
          </div>
        </div>
      </motion.div>

      {/* Content Options */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="glass-effect rounded-lg p-6"
      >
        <h3 className="text-lg font-semibold text-white mb-4">
          {isCodeFile ? 'Code Analysis Options' : 'Content Options'}
        </h3>
        
        <div className="grid md:grid-cols-2 gap-4 mb-6">
          {!isCodeFile && (
            <button
              onClick={() => handleGetContent('full')}
              disabled={loading}
              className={`
                p-4 rounded-lg border-2 transition-all duration-300 text-left
                ${contentType === 'full' 
                  ? 'border-blue-400 bg-blue-400/20' 
                  : 'border-white/30 hover:border-white/50 bg-white/10'
                }
                ${loading ? 'opacity-50 cursor-not-allowed' : ''}
              `}
            >
              <h4 className="font-semibold text-white mb-2">Full Content</h4>
              <p className="text-white/70 text-sm">Read the complete document content</p>
            </button>
          )}
          
          <button
            onClick={() => handleGetContent('summary')}
            disabled={loading}
            className={`
              p-4 rounded-lg border-2 transition-all duration-300 text-left
              ${contentType === 'summary' 
                ? 'border-blue-400 bg-blue-400/20' 
                : 'border-white/30 hover:border-white/50 bg-white/10'
              }
              ${loading ? 'opacity-50 cursor-not-allowed' : ''}
            `}
          >
            <h4 className="font-semibold text-white mb-2">
              {isCodeFile ? 'Code Explanation' : 'Summary'}
            </h4>
            <p className="text-white/70 text-sm">
              {isCodeFile 
                ? 'Get plain English explanation of the code functionality'
                : 'Get AI-powered summary of the document'
              }
            </p>
          </button>
        </div>

        {/* Audio Controls */}
        {content && (
          <div className="space-y-4">
            <div className="flex items-center space-x-4">
              <button
                onClick={handleGenerateAudio}
                disabled={audioLoading}
                className="flex items-center space-x-2 px-4 py-2 bg-green-600 hover:bg-green-700 rounded-lg text-white transition-colors disabled:opacity-50"
              >
                {audioLoading ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <Volume2 className="w-4 h-4" />
                )}
                <span>{audioLoading ? 'Generating...' : 'Generate Audio'}</span>
              </button>

              {audioUrl && (
                <>
                  <button
                    onClick={handleAudioPlay}
                    className="flex items-center space-x-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-white transition-colors"
                  >
                    {isPlaying ? (
                      <VolumeX className="w-4 h-4" />
                    ) : (
                      <Volume2 className="w-4 h-4" />
                    )}
                    <span>{isPlaying ? 'Pause Audio' : 'Play Audio'}</span>
                  </button>

                  <button
                    onClick={handleDownloadAudio}
                    className="flex items-center space-x-2 px-4 py-2 bg-purple-600 hover:bg-purple-700 rounded-lg text-white transition-colors"
                  >
                    <Download className="w-4 h-4" />
                    <span>Download</span>
                  </button>

                  <div className="relative speed-control-container">
                    <button
                      onClick={() => setShowSpeedControl(!showSpeedControl)}
                      className="flex items-center space-x-2 px-4 py-2 bg-orange-600 hover:bg-orange-700 rounded-lg text-white transition-colors"
                    >
                      <Settings className="w-4 h-4" />
                      <span>{playbackSpeed}x</span>
                    </button>

                    {showSpeedControl && (
                      <motion.div
                        initial={{ opacity: 0, y: dropdownDirection === 'down' ? -10 : 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: dropdownDirection === 'down' ? -10 : 10 }}
                        className={`
                          absolute ${dropdownDirection === 'down' ? 'top-full mt-2' : 'bottom-full mb-2'} 
                          right-0 bg-white/20 backdrop-blur-md rounded-lg p-2 min-w-[140px] 
                          max-h-[300px] overflow-y-auto z-50 shadow-2xl border border-white/30
                        `}
                        style={{ zIndex: 9999 }}
                      >
                        <div className="space-y-1">
                          <div className="text-xs text-white/70 px-3 py-1 border-b border-white/20 mb-2">
                            Playback Speed
                          </div>
                          {speedOptions.map((option) => (
                            <button
                              key={option.value}
                              onClick={() => handleSpeedChange(option.value)}
                              className={`
                                w-full text-left px-3 py-2 rounded text-sm transition-colors flex items-center justify-between
                                ${playbackSpeed === option.value 
                                  ? 'bg-blue-600 text-white shadow-md' 
                                  : 'text-white hover:bg-white/20'
                                }
                              `}
                            >
                              <span>{option.label}</span>
                              {playbackSpeed === option.value && (
                                <span className="text-xs">✓</span>
                              )}
                            </button>
                          ))}
                          <div className="text-xs text-white/50 px-3 py-1 border-t border-white/20 mt-2">
                            {speedOptions.length} speed options
                          </div>
                        </div>
                      </motion.div>
                    )}
                  </div>
                </>
              )}
            </div>

            {/* Audio Progress Bar */}
            {audioUrl && (
              <div className="bg-white/10 rounded-lg p-4">
                <div className="flex items-center justify-between text-sm text-white/70 mb-3">
                  <span>Audio Player</span>
                  <span>Speed: {playbackSpeed}x</span>
                </div>
                
                <div className="space-y-3">
                  {/* Progress Bar */}
                  <div 
                    className="w-full bg-white/20 rounded-full h-3 cursor-pointer relative"
                    onClick={handleProgressClick}
                  >
                    <div 
                      className="bg-gradient-to-r from-blue-500 to-purple-500 h-3 rounded-full transition-all duration-300 relative"
                      style={{ width: duration ? `${(currentTime / duration) * 100}%` : '0%' }}
                    >
                      <div className="absolute right-0 top-1/2 transform translate-x-1/2 -translate-y-1/2 w-4 h-4 bg-white rounded-full shadow-lg"></div>
                    </div>
                  </div>
                  
                  {/* Time Display */}
                  <div className="flex items-center justify-between text-xs text-white/70">
                    <span>{formatTime(currentTime)}</span>
                    <div className="flex items-center space-x-4">
                      <span className={`px-2 py-1 rounded ${isPlaying ? 'bg-green-600' : 'bg-gray-600'}`}>
                        {isPlaying ? '▶ Playing' : '⏸ Paused'}
                      </span>
                      <span>{formatTime(duration)}</span>
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        )}
      </motion.div>

      {/* Content Display */}
      {(loading || content) && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="glass-effect rounded-lg p-6"
        >
          <h3 className="text-lg font-semibold text-white mb-4">
            {isCodeFile ? 'Code Explanation' : contentType === 'full' ? 'Full Content' : 'Summary'}
          </h3>
          
          {loading ? (
            <div className="flex flex-col items-center justify-center py-12 space-y-4">
              <Loader2 className="w-12 h-12 text-white animate-spin" />
              <div className="text-center">
                <p className="text-xl font-semibold text-white">Processing with AI...</p>
                <p className="text-sm text-white/70 mt-2">
                  {isCodeFile 
                    ? 'Analyzing code structure and generating explanation...'
                    : contentType === 'summary' 
                      ? 'Extracting key points and creating summary...'
                      : 'Extracting complete content from document...'
                  }
                </p>
              </div>
            </div>
          ) : (
            <div className="bg-white/10 rounded-lg p-6 max-h-96 overflow-y-auto">
              <p className="text-white leading-relaxed whitespace-pre-wrap text-justify">
                {content}
              </p>
            </div>
          )}
        </motion.div>
      )}
      
      {/* Hidden Audio Element */}
      {audioUrl && (
        <audio
          ref={audioRef}
          src={audioUrl}
          onEnded={() => setIsPlaying(false)}
          onPlay={() => setIsPlaying(true)}
          onPause={() => setIsPlaying(false)}
          onTimeUpdate={handleTimeUpdate}
          onLoadedMetadata={handleLoadedMetadata}
          className="hidden"
        />
      )}
    </div>
  );
};

export default ContentDisplay;