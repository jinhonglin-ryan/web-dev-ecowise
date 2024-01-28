import React, { useState } from 'react';
import ImageUploadComponent from './ImageUploadComponent';
import GameComponent from './GameComponent';
import ChatComponent from './ChatComponent';
import axios from 'axios';

function MainChatComponent() {
    const [mode, setMode] = useState('');
    const [textResponse, setTextResponse] = useState('');

    const handleChoiceSelected = (choice) => {
        const username = localStorage.getItem('username');
        // Send both username and choice to the backend
        axios.post('/game_check', { username, choice })
            .then(response => {
                setTextResponse(response.data.response);
            })
            .catch(error => {
                console.error("Error submitting choice", error);
            });
    };

    const handleModeChange = (newMode) => {
    setMode(newMode);
    // Send mode change to the API
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
        })
        .catch(error => {
        });
    };

    return (
    <div>
        <ImageUploadComponent onModeChange={handleModeChange} setTextResponse={setTextResponse} />
        {textResponse && <div>{textResponse}</div>}

        {mode === 'game' && <GameComponent onChoiceSelected={handleChoiceSelected} />}
        {mode === 'chat' && <ChatComponent />}
    </div>
    );
}

export default MainChatComponent;