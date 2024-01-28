import React, { useState } from 'react';
import ImageUploadComponent from './ImageUploadComponent';
import GameComponent from './GameComponent';
import ChatComponent from './ChatComponent';


const MainPageComponent = () => {
  const [mode, setMode] = useState('');
  const [textResponse, setTextResponse] = useState('');

  const handleModeChange = (newMode) => {
    setMode(newMode);
  };

  return (
    <div className="main-page">
      <ImageUploadComponent onModeChange={handleModeChange} setTextResponse={setTextResponse} />
      {textResponse && <div className="text-response">{textResponse}</div>}

      {mode === 'game' && <GameComponent />}
      {mode === 'chat' && <ChatComponent />}
    </div>
  );
};

export default MainPageComponent;
