import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './FullPageMapWithNav.css'; // Import your stylesheet


const RankComponent = () => {
    const [rankings, setRankings] = useState([]);

    useEffect(() => {
    axios.get('/rank_api')
        .then(response => {
        setRankings(response.data);
        console.log(response.data)
        })
        .catch(error => {
        console.error('Error fetching rankings:', error);
        });
    }, []);

    return (
      <div>
      <nav className="nav flex-column custom-nav" style={{
        position: 'absolute',
        top: '50%',
        left: '0',
        transform: 'translateY(-50%)',
        height: '100%', // Take full height to align items in the middle
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center', // This centers the links vertically
        zIndex: 2
      }}>
        <a href="http://10.150.243.90:3000/whyus">Why Us</a>
        <a href="http://localhost:3000/main">Chat</a>
        <a href="http://10.150.243.90:3000/game">Game</a>
        <a href="http://10.150.243.90:3000/rank">Rank</a>
        <a href="#">Contact</a>
      </nav>

      <div className="content-container">
        <div className="h1-container">
            <h1>College Rankings</h1>
        </div>
          <table className="table">
          <thead>
            <tr>
              <th scope="col">Rank</th>
              <th scope="col">College Name</th>
              <th scope="col">Score</th>
            </tr>
          </thead>
          <tbody className="table-group-divider">
          {rankings.map((ranking, index) => (
              <tr scope="row">
                <td>{index + 1}</td>
                <td>{ranking.college_name}</td>
                <td>{ranking.college_score}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      </div>
    );
};

export default RankComponent;