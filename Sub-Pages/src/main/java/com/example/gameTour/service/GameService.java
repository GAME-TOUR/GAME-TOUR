package com.example.gameTour.service;

import com.example.gameTour.model.Game;
import org.springframework.stereotype.Service;

import java.util.Arrays;
import java.util.List;

@Service
public class GameService {
    public List<Game> getGames() {
        return Arrays.asList(
                new Game(1, "Baldur's Gate 3", "Story-rich, party-based RPG set in the universe of Dungeons & Dragons", 9.5, "https://steamcdn-a.akamaihd.net/steam/apps/1086940/library_600x900_2x.jpg"),
                new Game(2, "PUBG: BATTLEGROUNDS", "Squad up and join the Battlegrounds for the original Battle Royale experience.", 9.7, "https://steamcdn-a.akamaihd.net/steam/apps/578080/library_600x900_2x.jpg"),
                new Game(3, "Witcher 3: Wild Hunt", "Action role-playing game set in a fantasy universe.", 9.9, "https://steamcdn-a.akamaihd.net/steam/apps/292030/library_600x900_2x.jpg")
        );
    }
}
