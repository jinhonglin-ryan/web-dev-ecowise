import React, { useState, useEffect } from 'react';
import axios from 'axios';

function GameComponent({ onChoiceSelected }) {
  const [questionData, setQuestionData] = useState({ question: '', choices: [] });

  useEffect(() => {
    const fetchGameData = async () => {
      try {
        const username = localStorage.getItem('username'); 
        const gameInitResponse = await axios.post('/api/game/init', { signal: 'yes', username });

        // Expecting a response with 'question' and 'choices'
        setQuestionData({
          question: gameInitResponse.data.question,
          choices: gameInitResponse.data.choices
        });
      } catch (error) {
        console.error("Error initiating game", error);
      }
    };

    fetchGameData();
  }, []);

  return (
    <div>
      <h3>{questionData.question}</h3>
      {questionData.choices.map((choice, index) => (
        <div key={index}>
          <button onClick={() => onChoiceSelected(String.fromCharCode(65 + index))}>
            {String.fromCharCode(65 + index)}
          </button> {choice}
        </div>
      ))}
    </div>
  );
}

export default GameComponent;
