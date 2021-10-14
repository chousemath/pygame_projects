from enum import Enum

SCREEN_WIDTH: int = 1_000
SCREEN_HEIGHT: int = 600


class GameState(Enum):
    START_MENU = 1
    IN_LEVEL = 2
    QUIT = 3


class LevelState(Enum):
    PLAY = 1
    CORRECT = 2
    WRONG = 3
