import React, { useState, useEffect } from 'react';
import axios from 'axios';

function GameComponent({ onAnswerSelected }) {
  const [question, setQuestion] = useState('');
  const [answers, setAnswers] = useState([]);
  const [selectedAnswer, setSelectedAnswer] = useState(null);

  useEffect(() => {
    // Replace with your actual API endpoint
    const fetchGameData = async () => {
      try {
        const questionResponse = await axios.get('/game/question');
        setQuestion(questionResponse.data.question);

        const answersResponse = await axios.get('/game/answers');
        setAnswers(answersResponse.data.answers);
      } catch (error) {
        console.error("Error fetching game data", error);
      }
    };

    fetchGameData();
  }, []);

  const handleAnswerClick = (answer) => {
    setSelectedAnswer(answer);
    onAnswerSelected(answer); // This function should handle the API call to validate the answer
  };

  return (
    <div>
      <h3>{question}</h3>
      {answers.map((answer, index) => (
        <button
          key={index}
          onClick={() => handleAnswerClick(answer)}
          style={{
            border: answer === selectedAnswer ? '3px solid blue' : '1px solid gray',
            margin: '5px',
            backgroundColor: answer === selectedAnswer ? '#D3D3D3' : 'white'
          }}
        >
          {answer}
        </button>
      ))}
    </div>
  );
}

export default GameComponent;
