import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import '../App.css';

const SignupComponent = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [collegeName, setCollegeName] = useState(''); 

    const handleSignup = async (e) => {
        e.preventDefault();
        try {
            // Your API call logic here
            const response = await axios.post('/register', { username, password, collegeName });
            console.log(response.data);
        } catch (error) {
            console.error("Signup failed", error);
        }
    };
    
    return (
        <div className="form-container" style={{ marginTop: '20px' }}>
            <form onSubmit={handleSignup}>
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
                <select 
                    className="form-input" 
                    value={collegeName} 
                    onChange={(e) => setCollegeName(e.target.value)}
                >
                    <option value="">Select College</option> 
                    <option value="College of Arts & Sciences">College of Arts & Sciences</option>
                    <option value="Georgetown Law">Georgetown Law</option>
                    <option value="McCourt School of Public Policy">McCourt School of Public Policy</option>
                    <option value="McDonough School of Business">McDonough School of Business</option>
                    <option value="School of Medicine">School of Medicine</option>
                    <option value="School of Nursing">School of Nursing</option>
                    <option value="School of Health">School of Health</option>
                </select>
                <button className="form-button" type="submit">Signup</button>
                <p>
                    Already have an account? <Link to="/">Back to Log in</Link>
                </p>
            </form>
        </div>
    );
};

export default SignupComponent;