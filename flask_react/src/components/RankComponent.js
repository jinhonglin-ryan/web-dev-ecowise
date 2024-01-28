import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';



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
        <h1>College Rankings</h1>
          <table className="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">College Name</th>
              <th scope="col">Rank</th>
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
    );
};

export default RankComponent;