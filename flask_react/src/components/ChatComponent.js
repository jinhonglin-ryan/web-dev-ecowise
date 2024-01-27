import React, { useState } from 'react';
import axios from 'axios';

const ChatComponent = () => {
    const [messages, setMessages] = useState([]);
    const [inputText, setInputText] = useState('');

    const sendMessage = async () => {
        const newMessages = [...messages, { text: inputText, sender: 'user' }];
        setMessages(newMessages);
        setInputText('');

        const response = await axios.post('/api/chat', { message: inputText });
        setMessages([...newMessages, { text: response.data.reply, sender: 'bot' }]);
    };

    return (
        <div>
            <div>
                {messages.map((message, index) => (
                    <p key={index} style={{ textAlign: message.sender === 'bot' ? 'left' : 'right' }}>
                        {message.text}
                    </p>
                ))}
            </div>
            <input 
                type="text" 
                value={inputText} 
                onChange={(e) => setInputText(e.target.value)}
                onKeyDown={(e) => { if (e.key === 'Enter') sendMessage(); }}
            />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default ChatComponent;