import React, { useState } from 'react';
import ImageUploadComponent from './ImageUploadComponent';
import GameComponent from './GameComponent';
import ChatComponent from './ChatComponent';
import axios from 'axios';

const MainPageComponent = () => {
  const [mode, setMode] = useState('');
  const [textResponse, setTextResponse] = useState('');
  const [backendMessage, setBackendMessage] = useState('');

  const handleModeChange = (newMode) => {
    setMode(newMode);
    if (newMode === 'game') {
    }
  };

  const handleChoiceSelected = (answer) => {
    const username = localStorage.getItem('username');
    //返回用户答案
    axios.post('/game_check', { username, answer })
      .then(response => {
        setTextResponse(response.data.response);
        setBackendMessage(response.data.message);
      })
      .catch(error => {
        console.error("Error submitting choice", error);
      });
  };

  return (
    <div className="main-page">
      <ImageUploadComponent onModeChange={handleModeChange} setTextResponse={setTextResponse} />
      {textResponse && <div className="text-response">{textResponse}</div>}
      {backendMessage && <div className="backend-message">{backendMessage}</div>}

      {mode === 'game' && <GameComponent onChoiceSelected={handleChoiceSelected} />}
      {mode === 'chat' && <ChatComponent />}
    </div>
  );
};

export default MainPageComponent;