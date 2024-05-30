import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import GameListPage from './GameListPage';
import GameDetailPage from './GameDetailPage'; // GameDetailPage 컴포넌트를 추가해야 합니다.

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<GameDetailPage />} />
                    <Route path="/game/:gameId" element={<GameListPage />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
