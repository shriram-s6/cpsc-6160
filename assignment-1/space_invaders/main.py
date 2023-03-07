import pygame
from game_loops import GameLoop


if __name__ == '__main__':
    game_loop = GameLoop()
    game_loop.start_intro_loop(False)
    # end the game
    pygame.quit()
 