import sys
import pygame
import constants
import game_setup
import game_utils
import leaderboard
from prompt import Prompt
from space_invaders import Game


def game_intro_loop(game, restart_game=False):
    # Start a new game if restart_game is True
    if restart_game:
        game = Game(game_setup.spaceship, game_setup.aliens, game_setup.spaceship_bullets, game_setup.alien_bullets,
                    game_setup.display_surface, 'Shriram')
        game.start_new_round()
        main_game_loop(game)

    pygame.display.set_caption('Space Invaders')
    player_name_input_text = Prompt('Name:').prompt_text
    player_name_input_rect = player_name_input_text.get_rect()
    player_name_input_rect.center = (game_setup.window_width // 2 - 100, 275)

    player_name_font = pygame.font.Font(constants.TEXT_FONT, 32)
    player_name_rect = pygame.Rect(game_utils.get_start_quit_button_coords()[1], 250, 300, 50)
    pygame.draw.rect(game_setup.display_surface, (255, 255, 255), player_name_rect)

    # Set up the velocity of the button
    velocity = [0, 5]
    start_pos = game_setup.start_button.rect.centery
    intro_loop_running = True
    # Start the game intro loop
    while intro_loop_running:

        game_setup.display_surface.blit(game_setup.background, (0, 0))
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle button clicks
                mouse_position = pygame.mouse.get_pos()
                if game_setup.start_button.rect.collidepoint(mouse_position):
                    game.space_ship.lives = 5
                    game.round_number = 1
                    game.score = 0
                    main_game_loop(game)
                elif game_setup.quit_button.rect.collidepoint(mouse_position):
                    pygame.quit()
                    sys.exit()
                elif game_setup.leaderboard_button.rect.collidepoint(mouse_position):
                    leaderboard_loop(game)
                    intro_loop_running = False
                elif game_setup.controls_button.rect.collidepoint(mouse_position):
                    show_controls_screen()
                elif game_setup.music_button.rect.collidepoint(mouse_position):
                    if not game_setup.game_music_controller.music_on:
                        game_setup.music_button.text = 'ON'
                        game_setup.music_button.active_color = (0, 255, 0)
                        game_setup.music_button.inactive_color = (0, 200, 0)
                        game_setup.game_music_controller.toggle_music()
                    else:
                        game_setup.music_button.text = 'OFF'
                        game_setup.music_button.active_color = (255, 0, 0)
                        game_setup.music_button.inactive_color = (255, 0, 0)
                        game_setup.game_music_controller.toggle_music()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    game.space_ship.name = game.space_ship.name[:-1]
                elif event.key == pygame.K_RETURN:
                    game.space_ship.name = game.space_ship.name
                else:
                    game.space_ship.name += event.unicode

        # Move the button
        game_setup.start_button.rect.move_ip(velocity)

        # Bounce the button from its start position
        if game_setup.start_button.rect.centery <= start_pos - 30 or game_setup.start_button.rect.centery >= start_pos + 30:
            velocity[1] = -velocity[1]
            # Move the button back to its start position
            game_setup.start_button.rect.centery = start_pos

        # Update the screen
        game_setup.display_surface.blit(game_setup.background, (0, 0))
        game_setup.display_surface.blit(game_setup.welcome_text, game_setup.welcome_text_rect)
        game_setup.display_surface.blit(game_setup.created_by_text, game_setup.created_by_text_rect)
        game_setup.display_surface.blit(player_name_input_text, player_name_input_rect)
        game_setup.display_surface.blit(game_setup.music_text, game_setup.music_text_rect)
        game_setup.music_button.draw(game_setup.display_surface)
        game_setup.leaderboard_button.draw(game_setup.display_surface)
        game_setup.controls_button.draw(game_setup.display_surface)
        game_setup.start_button.draw(game_setup.display_surface)
        game_setup.quit_button.draw(game_setup.display_surface)
        pygame.draw.rect(game_setup.display_surface, (255, 255, 255), player_name_rect)
        text_surface = player_name_font.render(game.space_ship.name, True, '#6b7280')
        game_setup.display_surface.blit(text_surface, (player_name_rect.x + 5, player_name_rect.y + 5))

        pygame.display.update()
        # Wait for a short amount of time
        tick = pygame.time.Clock()
        tick.tick(20)


def main_game_loop(game):
    # Start the main game loop
    pygame.display.set_caption('Space Invaders Game')

    main_loop_running = True
    while main_loop_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if game_utils.show_confirm_quit_prompt(game):
                    game.score = 0
                    game.round_number = 1
                    game.space_ship.lives = 5
                    game_intro_loop(game, False)
                    main_loop_running = False
                else:
                    game_intro_loop(game, True)
                    main_loop_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_setup.spaceship.fire()

        # Update the game state and the screen
        game_setup.display_surface.blit(game_setup.background, (0, 0))
        game_setup.spaceships.update()
        game_setup.spaceships.draw(game_setup.display_surface)
        game_setup.aliens.update()
        game_setup.aliens.draw(game_setup.display_surface)
        game_setup.spaceship_bullets.update()
        game_setup.spaceship_bullets.draw(game_setup.display_surface)
        game_setup.alien_bullets.update()
        game_setup.alien_bullets.draw(game_setup.display_surface)
        game.update()
        game.draw()
        pygame.display.update()
        game_setup.clock.tick(constants.FPS)


def leaderboard_loop(game):
    game_setup.display_surface.blit(game_setup.background, (0, 0))
    pygame.display.set_caption('Leaderboard')
    scores = leaderboard.read_scores()
    scores = sorted(scores, key=lambda score: score['score'], reverse=True)

    leaderboard_display = True
    # Define the table headers
    headers = ['Position', 'Player', 'Score']
    # Define the size of the table
    table_width = 800
    table_height = 800
    cell_padding = 5

    # Define the size of the cells
    cell_width = int(table_width / len(headers))
    cell_height = int(table_height / (len(scores) + 1)) - 60

    header_font = pygame.font.Font(constants.TEXT_FONT, 32)

    while leaderboard_display:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leaderboard_display = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle button clicks
                mouse_position = pygame.mouse.get_pos()
                if game_setup.back_button.rect.collidepoint(mouse_position):
                    game_intro_loop(game, False)
                    leaderboard_display = False

        # Draw the table headers
        for index, header in enumerate(headers):
            header_text = header_font.render(header, True, (255, 255, 255))
            x = index * cell_width + cell_padding
            y = cell_padding
            game_setup.display_surface.blit(header_text,
                                            (constants.WINDOW_WIDTH // 2 - 400 + x,
                                             constants.WINDOW_HEIGHT // 2 - 200 - y))

        # Draw the table data
        for i, row in enumerate(scores[:10]):
            position_text = header_font.render(f'{i + 1}', True, (255, 255, 255))
            player_text = header_font.render(row['spaceship_name'], True, (255, 255, 255))
            score_text = header_font.render(str(row['score']), True, (255, 255, 255))

            x = cell_padding
            y = (i + 1) * cell_height + cell_padding
            game_setup.display_surface.blit(position_text,
                                            (constants.WINDOW_WIDTH // 2 - 400 + x,
                                             constants.WINDOW_HEIGHT // 2 - 200 - y))
            x += cell_width
            game_setup.display_surface.blit(player_text,
                                            (constants.WINDOW_WIDTH // 2 - 400 + x,
                                             constants.WINDOW_HEIGHT // 2 - 200 - y))
            x += cell_width
            game_setup.display_surface.blit(score_text,
                                            (constants.WINDOW_WIDTH // 2 - 400 + x,
                                             constants.WINDOW_HEIGHT // 2 - 200 - y))

            pygame.draw.line(game_setup.display_surface, constants.WHITE,
                             (table_width + 20, constants.WINDOW_HEIGHT // 2 - 200 - y),
                             (200, constants.WINDOW_HEIGHT // 2 - 200 - y), 2)
        # Draw the back button onto the leaderboard surface
        game_setup.back_button.draw(game_setup.display_surface)
        # Update the screen
        pygame.display.update()
        game_setup.clock.tick(constants.FPS)

def show_controls_screen():
    # Create the text for the controls screen
    title_font = pygame.font.Font(constants.TEXT_FONT, 50)
    title_text = title_font.render('Controls', True, constants.WHITE)
    title_rect = title_text.get_rect()
    title_rect.centerx = constants.WINDOW_WIDTH // 2
    title_rect.top = 50

    text_font = pygame.font.Font(constants.TEXT_FONT, 24)
    left_key = text_font.render('LEFT ARROW - Move Left', True, constants.WHITE)
    left_key_rect = left_key.get_rect()
    left_key_rect.centerx = constants.WINDOW_WIDTH // 2
    left_key_rect.top = 150
    
    right_key = text_font.render('RIGHT ARROW - Move Right', True, constants.WHITE)
    right_key_rect = right_key.get_rect()
    right_key_rect.centerx = constants.WINDOW_WIDTH // 2
    right_key_rect.top = left_key_rect.bottom + 30

    space_key = text_font.render('SPACE - Fire', True, constants.WHITE)
    space_key_rect = space_key.get_rect()
    space_key_rect.centerx = constants.WINDOW_WIDTH // 2
    space_key_rect.top = right_key_rect.bottom + 30

    # Show the controls screen
    controls_screen_running = True
    while controls_screen_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle button clicks
                mouse_position = pygame.mouse.get_pos()
                if game_setup.back_button.rect.collidepoint(mouse_position):
                    controls_screen_running = False

        # Update the screen
        game_setup.display_surface.blit(game_setup.background, (0, 0))
        game_setup.display_surface.blit(title_text, title_rect)
        game_setup.display_surface.blit(left_key, left_key_rect)
        game_setup.display_surface.blit(right_key, right_key_rect)
        game_setup.display_surface.blit(space_key, space_key_rect)
        game_setup.back_button.draw(game_setup.display_surface)

        pygame.display.update()
        tick = pygame.time.Clock()
        tick.tick(60)
