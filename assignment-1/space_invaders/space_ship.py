import os
import random
import pygame
import constants
from space_ship_bullet import SpaceshipBullet


class SpaceShip(pygame.sprite.Sprite):

    def __init__(self, bullets):
        super().__init__()
        self.image = pygame.image.load(os.getcwd() + '/assets/images/space-ship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = constants.WINDOW_WIDTH // 2
        self.rect.bottom = constants.WINDOW_HEIGHT
        self.lives = 5
        self.movement_speed = 8
        self.bullets = bullets

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.movement_speed
        if keys[pygame.K_RIGHT] and self.rect.right < constants.WINDOW_WIDTH:
            self.rect.x += self.movement_speed

    def fire(self):
        if len(self.bullets) < 2:
            SpaceshipBullet(self.rect.centerx, self.rect.top, self.bullets)
            if self.music_on:
                self.shoot_sound.play()
            return True
        return False

    def reset(self):
        self.rect.centerx = random.randint(self.image.get_width(), constants.WINDOW_WIDTH - self.image.get_width())
