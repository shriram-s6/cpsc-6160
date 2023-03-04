import random
import pygame
import game_utils
from alien_bullet import AlienBullet


class Alien(pygame.sprite.Sprite):
    """Class representing an alien in the game"""

    def __init__(self, x, y, velocity, bullets):
        super().__init__()

        # Load and scale alien image
        self.image = game_utils.get_scaled_image(pygame.image.load('assets/images/alien.png'), 0.75)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Store starting position of the alien
        self.starting_pos = (x, y)

        # Track which side the alien is moving
        self.direction = 1
        self.velocity = velocity
        self.bullets = bullets
        self.music_on = False
        self.shoot_sound = pygame.mixer.Sound('assets/music/alien_fire.wav')

    def update(self):
        """Update the position of the alien"""
        self.rect.x += self.direction * self.velocity

        # Randomly fire bullets
        if random.randint(0, 100) > 99 and len(self.bullets) < 2:
            if self.music_on:
                self.shoot_sound.play()
            self.fire()

    def fire(self):
        """Create a new AlienBullet object and add it to the bullets group"""
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullets)

    def reset(self):
        """Reset the position and direction of the alien to starting values"""
        self.rect.topleft = self.starting_pos
        self.direction = 1
