package com.example.gameTour.controller;

import com.example.gameTour.model.Game;
import com.example.gameTour.service.GameService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class GameController {
    @Autowired
    private GameService gameService;

    @GetMapping("/api/games")
    public List<Game> getGames() {
        return gameService.getGames();
    }

    @GetMapping("/api/hello")
    public String hello() {
        return "hello";
    }
}
