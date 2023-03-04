import pygame
from pygame.locals import *
from button import Button
import constants


def get_start_quit_button_coords():
    start_x_cord = (constants.WINDOW_WIDTH - 2 * constants.BUTTON_WIDTH) // 2
    quit_x_cord = start_x_cord + constants.BUTTON_WIDTH + 20

    return [start_x_cord, quit_x_cord]


def get_scaled_image(image, scale):
    scaled_width = int(image.get_width() * scale)
    scaled_height = int(image.get_height() * scale)
    transformed_image = pygame.transform.scale(image, (scaled_width, scaled_height))
    return transformed_image


def show_confirm_quit_prompt(game):
    button_one_x_cord, button_two_x_cord = get_start_quit_button_coords()
    yes_button = Button(
        x_cord=button_one_x_cord,
        y_cord=constants.BUTTON_Y_COORD,
        width=constants.BUTTON_WIDTH,
        height=constants.BUTTON_HEIGHT,
        inactive_color=(0, 255, 0),
        active_color=(0, 255, 0),
        text='Yes'
    )

    cancel_button = Button(
        x_cord=button_two_x_cord,
        y_cord=constants.BUTTON_Y_COORD,
        width=constants.BUTTON_WIDTH,
        height=constants.BUTTON_HEIGHT,
        inactive_color=(255, 0, 0),
        active_color=(255, 0, 0),
        text='Cancel'
    )

    # create font objects
    prompt_font = pygame.font.Font('assets/font/Poultrygeist.ttf', 32)

    # create text objects
    prompt_text = prompt_font.render(
        'Are you sure you want to quit?', True, constants.WHITE)

    # wait for user input
    show_prompt = True
    while show_prompt:

        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if yes_button.rect.collidepoint(mouse_pos):
                    return True
                elif cancel_button.rect.collidepoint(mouse_pos):
                    return False

        # draw prompt
        pygame.draw.rect(
            game.display_surface,
            constants.DARK_GRAY,
            (constants.WINDOW_WIDTH // 2 - 300, constants.WINDOW_HEIGHT // 2 - 200, 600, 300),
            border_radius=10
        )

        game.display_surface.blit(
            prompt_text,
            (constants.WINDOW_WIDTH // 2 - prompt_text.get_width() // 2, constants.WINDOW_HEIGHT // 2 - 150)
        )

        # draw buttons
        yes_button.draw(game.display_surface)
        cancel_button.draw(game.display_surface)
        pygame.display.update()
