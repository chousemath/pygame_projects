from enum import Enum
import pygame
from colors import Color
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class GameState(Enum):
    PLAY = 1
    WIN = 2
    LOSE = 3
    QUIT = 4

pygame.init()

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption('BREAKOUT!!!')

game_state = GameState.PLAY

while game_state == GameState.PLAY:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = GameState.QUIT

pygame.quit()
