from enum import Enum
import pygame as pyg


class Color(Enum):
    BLACK = (0, 0, 0)


class GameState(Enum):
    START_MENU = 1
    IN_LEVEL = 2
    QUIT = 3


class LevelState(Enum):
    PLAY = 1
    CORRECT = 2
    WRONG = 3


class Game:
    screen_width = 720 + 2 * 80
    screen_height = 720 + 2 * 80

    def __init__(self):
        dimensions = (self.screen_width, self.screen_height)
        self.screen = pyg.display.set_mode(dimensions)
        pyg.display.set_caption("Love you!")
        self.clock = pyg.time.Clock()
        self.fps = 60
        self.state = GameState.START_MENU

    def run(self):
        pyg.init()
        while self.state != GameState.QUIT:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.state = GameState.QUIT

            self.screen.fill(Color.BLACK.value)
            pyg.display.flip()
            self.clock.tick(self.fps)

        pyg.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
