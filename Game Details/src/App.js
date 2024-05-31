import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import GameListPage from './GameListPage';
import GameDetailPage from './GameDetailPage';
import SearchResultPage from "./SearchResultPage"; // GameDetailPage 컴포넌트를 추가해야 합니다.

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<SearchResultPage />}/>
                    {/*<Route path="/" element={<GameListPage />}/>*/}
                    <Route path="/game/:gameId" element={<GameDetailPage />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
