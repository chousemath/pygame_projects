from random import randrange
from pygame import Rect
from pygame.draw import rect
from colors import RED
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Apple:
    side = 10

    def __init__(self, snake):
        self.x = None
        self.y = None
        self.position = None
        self.find_position(snake)

    def find_position(self, snake):
        while self.position is None or self.position in snake.positions:
            self.x = randrange(0, SCREEN_WIDTH, 10)
            self.y = randrange(0, SCREEN_HEIGHT, 10)
            self.position = (self.x, self.y)

    def draw(self, screen, snake):
        collision = False
        if self.position in snake.positions:
            collision = True
            snake.extend()
        self.find_position(snake)
        rect(screen, RED, Rect(self.x, self.y, self.side, self.side))
        return collision
