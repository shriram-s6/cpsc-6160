import pygame
import game_loops
import game_setup
from space_invaders import Game

if __name__ == '__main__':
    game = Game(game_setup.spaceship, game_setup.aliens, game_setup.spaceship_bullets, game_setup.alien_bullets,
                game_setup.display_surface, 'Shriram')
    print(game.score)
    game.start_new_round()
    game_loops.game_intro_loop(game)
    # end the game
    pygame.quit()
