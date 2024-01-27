import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginComponent from './components/LoginComponent';
import SignupComponent from './components/SignupComponent';
import './App.css';
import MainPageComponent from './components/MainPageComponent';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={
          <>
            <div className="background-image"></div>
            <div className="georgetown-text">Georgetown</div>
            <LoginComponent />
          </>
        } />
        <Route path="/signup" element={
          <>
            <div className="background-image"></div>
            <div className="georgetown-text">Georgetown</div>
            <SignupComponent />
          </>
        } />
        <Route path="/main" element={<MainPageComponent />} />
      </Routes>
    </Router>
  );
};

export default App;