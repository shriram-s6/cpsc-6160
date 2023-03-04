import pygame
from pygame.rect import Rect
from constants import WHITE, TEXT_FONT, TEXT_FONT_SIZE


class Button:
    def __init__(self, x_cord, y_cord, width, height, inactive_color, active_color, text, font_color=WHITE):
        self.rect = Rect(x_cord, y_cord, width, height)
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text = text
        self.font = pygame.font.Font(TEXT_FONT, TEXT_FONT_SIZE)
        self.font_color = font_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.active_color, self.rect, border_radius=10)
        else:
            pygame.draw.rect(screen, self.inactive_color, self.rect, border_radius=10)
        text_surface = self.font.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
