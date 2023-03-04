import pygame
from pygame.sprite import Sprite

import constants


class AlienBullet(Sprite):
    """A class to represent an alien bullet"""

    def __init__(self, x_cord, y_cord, bullets):
        super().__init__()
        self.image = pygame.image.load('assets/images/red_bullet.png')
        self.rect = self.image.get_rect(center=(x_cord, y_cord))

        self.velocity = constants.BULLET_VELOCITY

        # Add bullet to the group of bullets passed
        bullets.add(self)

    def update(self):
        """Update the position of the bullet"""
        self.rect.y += self.velocity

        # Remove the bullet when it goes out of the screen
        if self.rect.top > constants.WINDOW_HEIGHT:
            self.kill()
