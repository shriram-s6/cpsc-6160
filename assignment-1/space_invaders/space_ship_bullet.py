import pygame
import constants


class SpaceshipBullet(pygame.sprite.Sprite):
    """A class representing a bullet fired by a spaceship in a game.

    Parameters:
        x_cord (int): The x-coordinate of the starting position of the bullet.
        y_cord (int): The y-coordinate of the starting position of the bullet.
        bullets (pygame.sprite.Group): A group of sprites containing all bullets in the game.

    Attributes:
        image (pygame.Surface): The image of the bullet.
        rect (pygame.Rect): The rectangular area occupied by the bullet.
        velocity (int): The speed at which the bullet moves vertically.

    """

    def __init__(self, x_cord, y_cord, bullets):
        super().__init__()
        self.image = pygame.image.load('assets/images/green_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x_cord
        self.rect.centery = y_cord

        self.velocity = constants.BULLET_VELOCITY
        bullets.add(self)

    def update(self):
        """Update the position of the bullet by moving it vertically."""
        self.rect.y -= self.velocity
        if self.rect.bottom < 0:
            self.kill()
