import sys
import pygame
import constants
import game_setup
import game_utils
import leaderboard
from space_invaders import Game

class GameLoop:
    def __init__(self):
        self.game = None
        self.clock = pygame.time.Clock()
        self.intro_loop_running = False
        self.main_loop_running = False
        self.display_leaderboard = False
        self.display_controlscreen = False
        self.font = pygame.font.Font(constants.TEXT_FONT, 32)
        
        # Set up game intro screen caption
        pygame.display.set_caption('Space Invaders')

    def start_intro_loop(self, restart_game=False):
        # Start a new game if restart_game is True
        if restart_game:
            self.start_new_game()
            self.start_main_loop()    

        self.start_new_game()
        self.show_player_name()

        # Set up the velocity of the button
        velocity = [0, 5]
        start_pos = game_setup.start_button.rect.centery
        self.intro_loop_running = True

        # Start the game intro loop
        while self.intro_loop_running:

            game_setup.display_surface.blit(game_setup.background, (0, 0))
            self.handle_game_intro_events()
            self.update_game_intro_screen(start_pos, velocity)
            
            
    def start_new_game(self):
        self.game = Game(game_setup.spaceship, game_setup.aliens, game_setup.spaceship_bullets, game_setup.alien_bullets,
                        game_setup.display_surface, self, 'Shriram')
        self.game.start_new_round()

    def show_player_name(self):
        pygame.draw.rect(game_setup.display_surface, (255, 255, 255), game_setup.player_name_rect)

    def handle_game_intro_events(self):
        # Handle game intro events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Handle button clicks
                    mouse_position = pygame.mouse.get_pos()
                    if game_setup.start_button.rect.collidepoint(mouse_position):
                        self.game.space_ship.lives = 5
                        self.game.round_number = 1
                        self.game.score = 0
                        self.start_main_loop()
                    elif game_setup.quit_button.rect.collidepoint(mouse_position):
                        pygame.quit()
                        sys.exit()
                    elif game_setup.leaderboard_button.rect.collidepoint(mouse_position):
                        self.show_leaderboard()
                    elif game_setup.controls_button.rect.collidepoint(mouse_position):
                        self.show_controls_screen()
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
                        self.game.space_ship.name = self.game.space_ship.name[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.game.space_ship.name = self.game.space_ship.name
                    else:
                        self.game.space_ship.name += event.unicode

    def update_game_intro_screen(self, start_pos, velocity):
        # Move the start button
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
        game_setup.display_surface.blit(game_setup.player_name_input_text, game_setup.player_name_input_rect)
        game_setup.display_surface.blit(game_setup.music_text, game_setup.music_text_rect)
        game_setup.music_button.draw(game_setup.display_surface)
        game_setup.leaderboard_button.draw(game_setup.display_surface)
        game_setup.controls_button.draw(game_setup.display_surface)
        game_setup.start_button.draw(game_setup.display_surface)
        game_setup.quit_button.draw(game_setup.display_surface)
        pygame.draw.rect(game_setup.display_surface, (255, 255, 255), game_setup.player_name_rect)
        text_surface = self.font.render(self.game.space_ship.name, True, '#6b7280')
        game_setup.display_surface.blit(text_surface, (game_setup.player_name_rect.x + 5, game_setup.player_name_rect.y + 5))

        pygame.display.update()
        self.clock.tick(20)
        

    def start_main_loop(self):
        # Start the main game loop
        pygame.display.set_caption('Space Invaders Game')

        self.main_loop_running = True
        while self.main_loop_running:
            self.handle_main_events()
            self.update_main_screen()
                
    def handle_main_events(self):
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                if game_utils.show_confirm_quit_prompt(self.game):
                    self.game.score = 0
                    self.game.round_number = 1
                    self.game.space_ship.lives = 5
                    self.start_intro_loop(False)
                    self.main_loop_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_setup.spaceship.fire()
    
    def update_main_screen(self):
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
        self.game.update()
        self.game.draw()
        pygame.display.update()
        game_setup.clock.tick(constants.FPS)

    def show_leaderboard(self):
        
        game_setup.display_surface.blit(game_setup.background, (0, 0))
        pygame.display.set_caption('Leaderboard')
        scores = leaderboard.read_scores()
        scores = sorted(scores, key=lambda score: score['score'], reverse=True)
        
        self.start_leaderboard_loop(scores)

    def start_leaderboard_loop(self, scores):
        
        self.display_leaderboard = True
        # Define the table headers
        headers = ['Position', 'Player', 'Score']
        # Define the size of the table
        table_width = 800
        table_height = 800
        cell_padding = 5

        # Define the size of the cells
        cell_width = int(table_width / len(headers))
        cell_height = int(table_height / (len(scores) + 1)) - 60

        header_font = self.font

        while self.display_leaderboard:
            
            self.handle_leaderboard_events()
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
            
            
    def handle_leaderboard_events(self):
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.display_leaderboard = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle button clicks
                mouse_position = pygame.mouse.get_pos()
                if game_setup.back_button.rect.collidepoint(mouse_position):
                    self.start_intro_loop(False)
                    self.display_leaderboard = False

    def show_controls_screen(self):

        # Show the controls screen
        self.display_controlscreen = True
        while self.display_controlscreen:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Handle button clicks
                    mouse_position = pygame.mouse.get_pos()
                    if game_setup.back_button.rect.collidepoint(mouse_position):
                        self.display_controlscreen = False

            # Update the screen
            game_setup.display_surface.blit(game_setup.background, (0, 0))
            game_setup.display_surface.blit(game_setup.controls_title_text, game_setup.controls_title_rect)
            game_setup.display_surface.blit(game_setup.left_key, game_setup.left_key_rect)
            game_setup.display_surface.blit(game_setup.right_key, game_setup.right_key_rect)
            game_setup.display_surface.blit(game_setup.space_key, game_setup.space_key_rect)
            game_setup.back_button.draw(game_setup.display_surface)

            pygame.display.update()
            tick = pygame.time.Clock()
            tick.tick(60)
