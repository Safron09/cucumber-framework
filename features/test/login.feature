# Created by Y.Safronnynov

Feature: Player login

  Scenario: Login with valid credentials
    Given Open the login page
    When Enter username "testplayer@example.com"
    And Enter password "ValidPass123"
    And Click login button
    Then Player is logged in successfully

  Scenario: Login with invalid credentials
    Given Open the login page
    When Enter username "testplayer@example.com"
    And Enter password "WrongPassword"
    And Click login button
    Then Error message is displayed
