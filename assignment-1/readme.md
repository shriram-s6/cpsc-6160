# CPSC 6160 2D Game Design

## Assignment One: Game Design of Space Invaders

Contributors: Shriram Sekar

This repository contains my submission for Assignment One of CPSC 6160 2D Game Design. In this assignment, I designed a 2D game based on the classic arcade game Space Invaders.

## Introduction

Space Invaders is a classic arcade video game that was released in 1978. It was designed by Tomohiro Nishikado and was one of the first shooting games ever created. In this game, the player controls a laser cannon and must shoot down waves of alien invaders that are descending towards the bottom of the screen. The game became very popular due to its addictive gameplay and simple yet effective design. It has since become a pop culture icon and has been referenced in numerous movies, TV shows, and other forms of media.

## Installation

OS Version: Windows 10

Python version: 3.11.0

Pygame version: 2.2.0

Run the following command to install the required packages.

`pip install -r requirements.txt`

## Instructions for running the game

1. Clone the repository to your local machine
2. Navigate to the cloned repository directory in your terminal/command prompt
3. Run `python main.py` from the space_invaders folder to start the game

## Game controls

* Use the left and right arrow keys to move the player's spaceship
* Press the space bar to shoot lasers at the invading aliens
* If the player's spaceship collides with an alien or an alien reaches the bottom of the screen, the game is over

## Motivation behind the game chosen:

Space Invaders is a classic arcade game many have enjoyed playing for years. The simplicity and challenge of the game inspired me to create my own version of it using Python and Pygame. As this is the first game I am developing, I wanted to build a game that's not easy or difficult but still allows me to learn about the basics of game development. I learned a lot about developing a simple game, which has given me the confidence to build more complex games.

## Reasoning behind the structure:

I structured the game using object-oriented programming principles to keep the code organized and modular. I created separate classes for the player, enemy, bullet objects. The game loop and event handling were implemented in the main GameLoop class. This approach allowed me to easily add new features and modify existing ones as needed.

The GameLoop class is responsible for starting and managing the game loops, and it contains instances of the Game, Prompt, and Button classes.

The Game class is responsible for managing the game state, including the player score, the player's spaceship, and the alien enemies. It contains instances of the SpaceshipBullet, AlienBullet, and Alien classes.

The Alien class is responsible for representing an enemy alien in the game. It contains information about the alien's position, health, and movement behavior.

The Button class is responsible for representing a clickable button on the screen. It contains information about the button's position, size, and text label.

The Prompt class is responsible for displaying text prompts on the screen. It contains information about the prompt's position, size, and text content.

The SpaceshipBullet class is responsible for representing a bullet fired by the player's spaceship. It contains information about the bullet's position, velocity, and damage.

The AlienBullet class is responsible for representing a bullet fired by an alien enemy. It contains information about the bullet's position, velocity, and damage.

Overall, the GameLoop class manages the game loops, while the Game class manages the game state and contains instances of other game-related classes. The Alien class represents enemy aliens, and the SpaceshipBullet and AlienBullet classes represent bullets fired by the player and aliens, respectively. Finally, the Prompt and Button classes are used for displaying text prompts and clickable buttons on the screen, respectively.

![image](https://user-images.githubusercontent.com/86624773/223579972-938d4229-5a92-4105-8f21-22dfe31d9038.png)

## Generalization

The game Space Invaders can be generalized to other types of games or applications by modifying the classes and functions to fit the specific requirements of the new game or application. For example, the player class can be modified to fit a platformer game by adding jumping and climbing abilities, while the enemy class can be modified to fit a tower defense game by adding different types of enemies with unique strengths and weaknesses.

The screenshot below is the Space Invaders introduction screen. The user can click start to directly start the game or change the game settings through other options.

![image](https://user-images.githubusercontent.com/86624773/223448810-21b0c4b2-2ba2-475e-8933-3b240bff2a67.png)

The user can change the username by editing the name user input field.

![image](https://user-images.githubusercontent.com/86624773/223518312-05a0dbe2-f6c8-42b3-a636-793698bf9752.png)

The user can click on the music toggle to turn the background and shoot music on or off.

![image](https://user-images.githubusercontent.com/86624773/223518383-2352a2e8-95a9-4a05-b745-c0fc5d2a90b4.png)

The user can click on the leaderboard button to see the top 10 scores in the game. The scores will be written into a CSV file, and the top 10 scores will be pulled from the CSV file every time the user visits the leaderboard.

![image](https://user-images.githubusercontent.com/86624773/223518458-280ace42-b71a-4a5a-a8b5-6a9e671794b9.png)

The user can click on the controls button to see the game controls.

![image](https://user-images.githubusercontent.com/86624773/223518528-97fd025c-a03d-4493-a601-7331125e3d26.png)

Once the user is familiar with the game controls and settings, the user can click the start button to play the game. The user can click the quit button to exit the game directly.

![image](https://user-images.githubusercontent.com/86624773/223518611-f68cc93b-c62c-4dd9-987c-9f802498051d.png)

A screenshot of the actual game.

![image](https://user-images.githubusercontent.com/86624773/223518757-535c9f3b-4ff6-4cf1-9565-3ea7525a5af7.png)

At any moment in the game, the user can click the quit or escape buttons to exit the game. The user will get a prompt to confirm if the user wants to quit the game, and the user can press the cancel button to continue playing the game.

![image](https://user-images.githubusercontent.com/86624773/223526235-a5940582-cc6c-493a-ae9f-2dd69190ff1b.png)

The game ends once the user loses all 5 lives. The user will see a prompt of the current game score and can restart the game or quit to proceed to the main menu.

![image](https://user-images.githubusercontent.com/86624773/223519723-7b256013-a996-411b-bd3d-ffddd103a84c.png)


## Future enhancements

There are several ways that the game can be further enhanced:

* Adding power-ups or upgrades that enhance player's spaceship
* Adding different types of aliens with unique abilities and behaviors
* Boss battles at the end of each level
