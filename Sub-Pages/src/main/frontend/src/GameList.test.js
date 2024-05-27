import React, { useState, useEffect } from 'react';
import './index.css';
import logo from './logo.svg';

// 각 게임 객체에 이미지 URL을 추가
const dummyGames = [
  {
    id: 1,
    title: "Baldur's Gate 3",
    description: "Story-rich, party-based RPG set in the universe of Dungeons & Dragons",
    rating: 9.5,
    imageUrl: "https://steamcdn-a.akamaihd.net/steam/apps/1086940/library_600x900_2x.jpg"
  },
  {
    id: 2,
    title: "PUBG: BATTLEGROUNDS",
    description: "Squad up and join the Battlegrounds for the original Battle Royale experience.",
    rating: 9.7,
    imageUrl: "https://steamcdn-a.akamaihd.net/steam/apps/578080/library_600x900_2x.jpg"
  },
  {
    id: 3,
    title: "Witcher 3: Wild Hunt",
    description: "Action role-playing game set in a fantasy universe.",
    rating: 9.9,
    imageUrl: "https://steamcdn-a.akamaihd.net/steam/apps/292030/library_600x900_2x.jpg"
  }
];

const GameList = () => {
  const [games, setGames] = useState([]);
  const [filteredGames, setFilteredGames] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    setGames(dummyGames);
    setFilteredGames(dummyGames);
  }, []);

  useEffect(() => {
    const results = games.filter(game =>
      game.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      game.description.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredGames(results);
  }, [searchTerm, games]);

  return (
      <div className="App">
        <div className="navbar">
          <div className="navbar-top">
            <img src={logo} alt="Logo" className="logo" />
          </div>
          <div className="navbar-bottom">
            <h1>Game Reviews</h1>
            <input
                type="text"
                placeholder="Search games..."
                value={searchTerm}
                onChange={e => setSearchTerm(e.target.value)}
                className="search-bar"
            />
          </div>
        </div>
        <div className="game-grid">
          {filteredGames.map(game => (
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