import React, { useState } from 'react';
import ImageUploadComponent from './ImageUploadComponent';
import GameComponent from './GameComponent';
import ChatComponent from './ChatComponent';
import axios from 'axios';

function MainChatComponent() {
  const [mode, setMode] = useState('');
  const [textResponse, setTextResponse] = useState('');

  const handleModeChange = (newMode) => {
    setMode(newMode);
    // Send mode change to the API if needed
    axios.post('/api/mode', { mode: newMode });
  };

  const handleAnswerSubmit = (answer) => {
    // Submit the answer to your API
    axios.post('/api/game/submit-answer', { answer });
  };
  const handleAnswerSelected = (answer) => {
    // Submit the selected answer to your API for validation
    axios.post('/api/game/validate-answer', { answer })
      .then(response => {
        // Handle the response (e.g., display if the answer is correct or not)
      })
      .catch(error => {
        // Handle any errors
      });
  };

  return (
    <div>
      <ImageUploadComponent onModeChange={handleModeChange} setTextResponse={setTextResponse} />
      {textResponse && <div>{textResponse}</div>}

      {mode === 'game' && <GameComponent onAnswerSelected={handleAnswerSelected} />}
      {mode === 'chat' && <ChatComponent />}
    </div>
  );
}

export default MainChatComponent;