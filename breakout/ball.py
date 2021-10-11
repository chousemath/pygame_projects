from pygame.sprite import Sprite
from pygame import Surface
from pygame.draw import rect
from colors import BLACK
from random import choice
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SPEED_X, BALL_SPEED_Y


class Ball(Sprite):
    def __init__(self, color, side, start_x, start_y):
        super().__init__()
        self.side = side
        self.image = Surface((side, side))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        rect(self.image, color, (0, 0, side, side))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.velocity_x = choice((-1, 1)) * BALL_SPEED_X
        self.velocity_y = -BALL_SPEED_Y

    def update(self):
        self.rect.x += self.velocity_x

        limit = SCREEN_WIDTH - self.side

        if self.rect.x > limit:
            self.rect.x = limit
            self.velocity_x *= -1
        elif self.rect.x < 0:
            self.rect.x = 0
            self.velocity_x *= -1

        self.rect.y += self.velocity_y

        limit = SCREEN_HEIGHT - self.side

        if self.rect.y > limit:
            self.rect.y = limit
            self.velocity_y *= -1
        elif self.rect.y < 0:
            self.rect.y = 0
            self.velocity_y *= -1
