import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import '../App.css'; 

const LoginComponent = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            // Your API call logic here
            const response = await axios.post('/login', { username, password });
            console.log(response.data);
            localStorage.setItem('username', username);
            navigate('/main');
        } catch (error) {
            console.error("Login failed", error);
        }
    };

    return (
        <div className="form-container">
            <form onSubmit={handleLogin}>
                <input 
                    className="form-input"
                    type="text" 
                    placeholder="Username" 
                    value={username} 
                    onChange={(e) => setUsername(e.target.value)} 
                />
                <input 
                    className="form-input"
                    type="password" 
                    placeholder="Password" 
                    value={password} 
                    onChange={(e) => setPassword(e.target.value)} 
                />
                <button className="form-button" type="submit">Login</button>
                <p>
                    Not signed up yet? <Link to="/signup">Sign up here</Link>
                </p>
            </form>
        </div>
    );
};

export default LoginComponent;
