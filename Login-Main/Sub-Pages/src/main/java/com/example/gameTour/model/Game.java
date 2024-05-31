package com.example.gameTour.model;

public class Game {
    private Integer id;
    private String title;
    private String description;
    private Double rating;
    private String imageUrl;

    public Game(Integer id, String title, String description, Double rating, String imageUrl) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.rating = rating;
        this.imageUrl = imageUrl;
    }

    // Getters and setters
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Double getRating() {
        return rating;
    }

    public void setRating(Double rating) {
        this.rating = rating;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }
}
