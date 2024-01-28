import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginComponent from './components/LoginComponent';
import SignupComponent from './components/SignupComponent';
import './App.css';
import MainPageComponent from './components/MainPageComponent';
import MapComponent from './components/MapComponent';
import Game from "./components/Game";
import RankComponent from "./components/RankComponent";


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={
          <div className="app-container">
            <div className="background-image"></div>
            <div className="georgetown-text">Georgetown</div>
            <LoginComponent />
          </div>
        } />
        <Route path="/signup" element={
          <div className="app-container">
            <div className="background-image"></div>
            <div className="georgetown-text">Georgetown</div>
            <SignupComponent />
          </div>
        } />
        <Route path="/main" element={
          <div className="app-container">
            <MainPageComponent />
          </div>
        } />
        <Route path="/whyus" element={<MapComponent />} />
        <Route path="/game" element={<Game />} />
        <Route path="/rank" element={<RankComponent />} />
      </Routes>
    </Router>
  );
};

export default App;