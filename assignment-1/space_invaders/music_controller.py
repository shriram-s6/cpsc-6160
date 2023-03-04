import os
import pygame
from alien import Alien
from space_ship import SpaceShip
from space_invaders import Game


class MusicController:
    def __init__(self) -> None:
        # load music files and set sounds

        Alien.shoot_sound = pygame.mixer.Sound(os.getcwd() + '/assets/music/spaceship_fire.wav')
        Alien.music_on = False
        SpaceShip.music_on = False
        Game.background_music = pygame.mixer.Sound(os.getcwd() + '/assets/music/background.wav')
        Game.progress_sound = pygame.mixer.Sound(os.getcwd() + '/assets/music/progress.wav')
        Game.breach_sound = pygame.mixer.Sound(os.getcwd() + '/assets/music/breach.wav')
        Game.alien_hit_sound = pygame.mixer.Sound(os.getcwd() + '/assets/music/alien_hit.wav')
        SpaceShip.shoot_sound = pygame.mixer.Sound(os.getcwd() + '/assets/music/spaceship_hit.wav')
        Game.background_music_on = False
        self.music_on = False

    
    def toggle_music(self):
        Alien.music_on = not Alien.music_on
        SpaceShip.music_on = not SpaceShip.music_on
        Game.background_music_on = not Game.background_music_on
        self.music_on = not self.music_on

        if self.music_on:
            Game.background_music.set_volume(0.2)
            Game.background_music.play(-1, 0)
            Alien.shoot_sound.set_volume(0.2)
            SpaceShip.shoot_sound.set_volume(0.2)
            Game.progress_sound.set_volume(0.2)
            Game.breach_sound.set_volume(0.2)
        else:
            Game.background_music.set_volume(0)
            Game.background_music.stop()