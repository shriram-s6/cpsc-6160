import pygame

import constants


class Prompt:
    def __init__(self, text, font_size=constants.TEXT_FONT_SIZE):
        self.font = pygame.font.Font(constants.TEXT_FONT, font_size)
        self.text = text
        self.prompt_text = self.font.render(self.text, True, constants.WHITE)
        self.prompt_rect = self.prompt_text.get_rect(center=(constants.WINDOW_WIDTH//2, constants.WINDOW_HEIGHT//2))

    def update_text(self, text):
        self.text = text
        self.prompt_text = self.font.render(self.text, True, constants.WHITE)
        self.prompt_rect = self.prompt_text.get_rect(center=(constants.WINDOW_WIDTH//2, constants.WINDOW_HEIGHT//2))
