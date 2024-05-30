import React from 'react';
//import { useParams } from 'react-router-dom';
import './GameDetailPage.css';
import HomeHeader from './HomeHeader';  // HomeHeader 컴포넌트 추가

const gamesData = [
    {
        id: '1',
        title: "Baldur's Gate 3",
        year: "2023",
        developer: "Larian Studios",
        description: "Baldur’s Gate 3 is a story-rich, party-based RPG set in the universe of Dungeons & Dragons, where your choices shape a tale of fellowship and betrayal, survival and sacrifice, and the lure of absolute power.",
        imageUrl: "https://steamcdn-a.akamaihd.net/steam/apps/1086940/library_600x900_2x.jpg",
        reviews: [
            { username: "JohnDoe", content: "Great game with deep story!", rating: 5 },
            { username: "JaneDoe", content: "Love the graphics and gameplay!", rating: 5 },
            { username: "Alex", content: "Well made!", rating: 4 },
            { username: "Sam", content: "Not bad", rating: 4 },
            { username: "Chris", content: "Not my style", rating: 2 }
        ],
        purchaseOptions: [
            { platform: "Steam", url: "https://store.steampowered.com/app/somegame" },
            { platform: "GOG", url: "https://gog.com/game/somegame" }
        ]
    }
];

function GameDetailPage() {
    // const { gameId } = useParams();
    const gameId = '1';
    const game = gamesData.find(game => game.id === gameId);
    const averageRating = game.reviews.reduce((acc, review) => acc + review.rating, 0) / game.reviews.length;

    const ratingCounts = game.reviews.reduce((acc, review) => {
        acc[review.rating] = (acc[review.rating] || 0) + 1;
        return acc;
    }, {});

    const maxReviews = Math.max(...Object.values(ratingCounts));
    const bars = Object.entries(ratingCounts).map(([rating, count]) => (
        <div key={rating} style={{ margin: '5px', textAlign: 'center' }}>
            <div style={{
                background: '#4a90e2',
                height: `${(count / maxReviews) * 100}%`,
                width: '20px'
            }} />
            {rating} star ({count})
        </div>
    ));

    function generateStars(rating) {
        return "★".repeat(rating);
    }

    if (!game) {
        return <div>Game not found</div>;
    }

    return (
        <div className="App">
            <HomeHeader />
            <div className="game-detail">
                <div className="game-data">
                    <div className="first-row">
                        <div className="game-banner">
                            <img src={game.imageUrl} alt={`Cover of ${game.title}`} />
                        </div>
                        <div className="purchase-options">
                            {game.purchaseOptions.map(option => (
                                <a key={option.platform} href={option.url} target="_blank" rel="noopener noreferrer">
                                    | Buy on {option.platform} |
                                </a>
                            ))}
                        </div>
                    </div>
                    <div className="second-row">
                        <div className="game-info">
                            <h1>{game.title}</h1>
                            <h4>{game.year} | {game.developer}</h4>
                            <p>{game.description}</p>
                        </div>
                        <div className="game-rating">
                            <h2>Average Rating: {averageRating.toFixed(1)}</h2>
                            <div className="rating-bar-container">
                                {Array.from({length: 5}, (_, i) => i + 1).map(score => (
                                    <div key={score} className="rating-bar"
                                         style={{height: `${(ratingCounts[score] || 0) / maxReviews * 100}%`}}>
                                        <span
                                            className="rating-text">{generateStars(score)} ({ratingCounts[score] || 0})</span>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
                <div className="game-reviews">
                    {game.reviews.map((review, index) => (
                        <div key={index} className="review-item">
                            <h3>{review.username}</h3>
                            <p>{review.content}</p>
                            <p>Rating: {review.rating}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default GameDetailPage;