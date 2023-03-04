import pygame
import game_utils
from button import Button
from menu_cursors import MenuCursor
from prompt import Prompt
from space_ship import SpaceShip
import constants

# Initialize Pygame
pygame.mixer.init()
pygame.font.init()

# Set display surface
window_width = constants.WINDOW_WIDTH
window_height = constants.WINDOW_HEIGHT
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Invaders')
background = pygame.image.load('assets/images/background.jpg')

# Set FPS and clock
FPS = constants.FPS
clock = pygame.time.Clock()

# Create bullets, spaceship group, and spaceship object
spaceship_bullets = pygame.sprite.Group()
alien_bullets = pygame.sprite.Group()
spaceships = pygame.sprite.Group()
spaceship = SpaceShip(spaceship_bullets)
spaceships.add(spaceship)

# Create aliens group
aliens = pygame.sprite.Group()

# Set up introduction screen elements
welcome_text = Prompt('Space Invaders', 128).prompt_text
welcome_text_rect = welcome_text.get_rect()
welcome_text_rect.center = (window_width // 2, 100)

created_by_text = Prompt('By Shriram').prompt_text
created_by_text_rect = created_by_text.get_rect()
created_by_text_rect.center = (window_width // 2, 180)

music_text = Prompt('Music:').prompt_text
music_text_rect = music_text.get_rect()
music_text_rect.center = (window_width // 2 - 100, 350)


start_button = Button(x_cord=game_utils.get_start_quit_button_coords()[0], y_cord=525, width=constants.BUTTON_WIDTH,
                      height=constants.BUTTON_HEIGHT, inactive_color='#00FF7F',
                      active_color=(0, 255, 0), text='Start', font_color=(255, 255, 255))

quit_button = Button(x_cord=game_utils.get_start_quit_button_coords()[1], y_cord=525, width=constants.BUTTON_WIDTH,
                     height=constants.BUTTON_HEIGHT, inactive_color='#DC143C',
                     active_color=(255, 0, 0), text='Quit', font_color=(255, 255, 255))

music_button = Button(x_cord=game_utils.get_start_quit_button_coords()[1], y_cord=325, width=constants.BUTTON_WIDTH,
                      height=constants.BUTTON_HEIGHT, inactive_color=(255, 0, 0),
                      active_color=(255, 0, 0), text='OFF')

leaderboard_button = Button(game_utils.get_start_quit_button_coords()[0], y_cord=400, width=constants.BUTTON_WIDTH + 100,
                      height=constants.BUTTON_HEIGHT + 10, inactive_color='#6b7280',
                      active_color='#6b7280', text='Leaderboard')

back_button = Button(50, y_cord=50, width=constants.BUTTON_WIDTH,
                      height=constants.BUTTON_HEIGHT, inactive_color='#6b7280',
                      active_color='#6b7280', text='Back')


# Set up music object and state variable
music = pygame.mixer.Sound('assets/music/progress.wav')
music.set_volume(0.5)
