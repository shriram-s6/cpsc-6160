import os
import pygame
import constants
import game_loops
import game_setup
import game_utils
import leaderboard
from alien import Alien
from button import Button
from prompt import Prompt


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Game:

    def __init__(self, space_ship, aliens, space_ship_bullet_group, alien_bullet_group, display_surface,
                 spaceship_name='Anonymous'):

        # define game variables
        self.round_number = 1
        self.score = 0
        self.display_surface = display_surface
        self.space_ship = space_ship
        self.space_ship.name = spaceship_name if len(spaceship_name) != 0 else 'Anonymous'
        self.aliens = aliens
        self.space_ship.lives = 5
        self.space_ship_bullet_group = space_ship_bullet_group
        self.alien_bullet_group = alien_bullet_group
        self.background = pygame.image.load('assets/images/background.jpg')
        self.music_on = False

        if self.music_on:
            self.set_music()

        # load music files and set sounds
        self.progress_sound = pygame.mixer.Sound(os.getcwd() + '/assets/music/progress.wav')
        self.breach_sound = pygame.mixer.Sound(os.getcwd() + '/assets/music/breach.wav')
        self.alien_hit_sound = pygame.mixer.Sound(os.getcwd() + '/assets/music/alien_hit.wav')
        self.spaceship_hit_sound = pygame.mixer.Sound(os.getcwd() + '/assets/music/spaceship_hit.wav')

        # load heart image
        self.full_heart = game_utils.get_scaled_image(pygame.image.load(os.getcwd() + '/assets/images/full_heart.png').convert_alpha(),
                                                      constants.SCALE)

        self.font = pygame.font.Font(constants.TEXT_FONT, constants.TEXT_FONT_SIZE)


    def update(self) -> None:

        self.move_aliens()
        self.check_collisions()
        self.check_round_completion()

    def draw(self) -> None:

        score_text = self.font.render('Score: ' + str(self.score), True, constants.WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = constants.WINDOW_WIDTH // 2
        score_rect.top = 10

        round_text = self.font.render('Round: ' + str(self.round_number), True, constants.WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)

        spaceship_name_text = self.font.render(f'{self.space_ship.name}', True, constants.WHITE)
        spaceship_name_text_rect = spaceship_name_text.get_rect()
        spaceship_name_text_rect.topleft = (constants.WINDOW_WIDTH - 300 - spaceship_name_text.get_width() , 10)

        self.display_surface.blit(score_text, score_rect)
        self.display_surface.blit(round_text, round_rect)
        self.display_surface.blit(spaceship_name_text, spaceship_name_text_rect)
        pygame.draw.line(self.display_surface, constants.WHITE, (0, 50), (constants.WINDOW_WIDTH, 50), 4)
        pygame.draw.line(self.display_surface, constants.WHITE, (0, constants.WINDOW_HEIGHT - 100),
                         (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT - 100), 4)

        for i in range(self.space_ship.lives):
            self.display_surface.blit(self.full_heart, (constants.WINDOW_WIDTH - 50 - i * 50, 0))

    def move_aliens(self):

        move = False
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0 or alien.rect.right >= constants.WINDOW_WIDTH:
                move = True

        if move:
            breach = False
            for alien in (self.aliens.sprites()):
                alien.rect.y += 10 * self.round_number

                alien.direction = -1 * alien.direction
                alien.rect.x += alien.direction * alien.velocity

                # check if an alien reached the ship
                if alien.rect.bottom >= constants.WINDOW_HEIGHT - 100:
                    breach = True

            # aliens breached the line
            if breach:
                if self.music_on:
                    self.breach_sound.play()
                self.space_ship.lives -= 1

    def check_collisions(self):
        if pygame.sprite.groupcollide(self.space_ship_bullet_group, self.aliens, True, True):
            if self.music_on:
                self.alien_hit_sound.play()
            self.score += 10

        # see if the player has collided with any bullet in the alien bullet group
        if pygame.sprite.spritecollide(self.space_ship, self.alien_bullet_group, True):
            if self.music_on:
                self.spaceship_hit_sound.play()
            self.space_ship.lives -= 1

        if self.space_ship.lives == 0:
            self.end_game()

    def check_round_completion(self):
        # a round ends, if there are no more aliens
        if not self.aliens:
            self.score += 100 * self.round_number
            self.round_number += 1

            self.start_new_round()

    def start_new_round(self):
        self.aliens.empty()
        for i in range(11):
            for j in range(5):
                alien = Alien(48 + i * 48, 48 + j * 48, self.round_number, self.alien_bullet_group)
                self.aliens.add(alien)

    def reset_game(self):

        self.aliens.empty()
        self.alien_bullet_group.empty()
        self.space_ship_bullet_group.empty()
        self.score = 0
        self.round_number = 1
        self.space_ship.lives = 5

    def end_game(self):

        self.space_ship.lives = 0
        button_one_x_cord = game_utils.get_start_quit_button_coords()[0]
        button_two_x_cord = game_utils.get_start_quit_button_coords()[1]

        yes_button = Button(x_cord=button_one_x_cord, y_cord=375, width=constants.BUTTON_WIDTH,
                            height=constants.BUTTON_HEIGHT, inactive_color=(0, 255, 0),
                            active_color=(0, 255, 0), text='Yes', font_color=(255, 255, 255))

        no_button = Button(x_cord=button_two_x_cord, y_cord=375, width=constants.BUTTON_WIDTH,
                           height=constants.BUTTON_HEIGHT, inactive_color=(255, 0, 0),
                           active_color=(255, 0, 0), text='No', font_color=(255, 255, 255))

        leaderboard.write_score(self.space_ship.name, self.score)

        # create text objects
        prompt_one_text = Prompt('Game Over').prompt_text
        prompt_two_text = Prompt(f'Final score - {self.score}').prompt_text
        prompt_three_text = Prompt('Do you want start a new game?').prompt_text

        show_prompt_loop = True
        # wait for user input
        while show_prompt_loop:
            # draw prompt
            pygame.draw.rect(self.display_surface, constants.DARK_GRAY,
                             (constants.WINDOW_WIDTH // 2 - 300, constants.WINDOW_HEIGHT // 2 - 200, 600, 350),
                             border_radius=10)

            self.display_surface.blit(prompt_one_text, (
                constants.WINDOW_WIDTH // 2 - prompt_one_text.get_width() // 2 + 10,
                constants.WINDOW_HEIGHT // 2 - 180))

            self.display_surface.blit(prompt_two_text, (
                constants.WINDOW_WIDTH // 2 - prompt_two_text.get_width() // 2 + 10,
                constants.WINDOW_HEIGHT // 2 - 120))

            self.display_surface.blit(prompt_three_text, (
                constants.WINDOW_WIDTH // 2 - prompt_three_text.get_width() // 2, constants.WINDOW_HEIGHT // 2 - 60))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if yes_button.rect.collidepoint(mouse_pos):
                        game = Game(game_setup.spaceship, game_setup.aliens, game_setup.spaceship_bullets,
                                    game_setup.alien_bullets,
                                    game_setup.display_surface, self.space_ship.name)
                        game.space_ship.lives = 5
                        game.round_number = 1
                        game.score = 0
                        show_prompt_loop = False
                        game.start_new_round()
                        game_loops.main_game_loop(game)

                    elif no_button.rect.collidepoint(mouse_pos):
                        self.space_ship.lives = 5
                        self.round_number = 1
                        self.score = 0
                        show_prompt_loop = False
                        game_loops.game_intro_loop(self)

            # draw buttons
            yes_button.draw(self.display_surface)
            no_button.draw(self.display_surface)
            pygame.display.update()

    def set_music(self):
        self.space_ship.music_on = True
