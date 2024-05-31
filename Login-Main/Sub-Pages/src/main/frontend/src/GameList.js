import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './index.css';
import logo from './logo.svg';

const GameList = () => {
  const [games, setGames] = useState([]);

  useEffect(() => {
    axios.get('/api/games')
        .then(response => {
          setGames(response.data);
        })
        .catch(error => console.error('Error fetching data: ', error));
  }, []);

  return (
      <div className="App">
        <div className="navbar">
          <div className="navbar-top">
            <img src={logo} alt="Logo" className="logo" />
          </div>
          <div className="navbar-bottom">
            <h1>Game Reviews</h1>
          </div>
        </div>
        <div className="game-grid">
          {games.map(game => (
              <div key={game.id} className="game-item">
                <img src={game.imageUrl} alt={`Cover of ${game.title}`} />
                <div className="game-details">
                  <h2>{game.title}</h2>
                  <p>{game.description}</p>
                  <p>Rating: {game.rating}</p>
                </div>
              </div>
          ))}
        </div>
      </div>
  );
};

export default GameList;
