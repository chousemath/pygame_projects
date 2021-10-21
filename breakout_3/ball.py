import pygame
from colors import Color
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BALL_SPEED_X,
    BALL_SPEED_Y,
)
from random import choice

class Ball(pygame.sprite.Sprite):
    def bounce(self):
        # clear the ball from the collision
        # territory of the paddle
        self.rect.x -= self.velocity_x
        self.rect.y -= self.velocity_y

        # reverse the y velocity
        self.velocity_y *= -1

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


    def __init__(self, color, side, start_x, start_y):
        super().__init__()
        self.side = side

        dimensions = (side, side)
        self.image = pygame.Surface(dimensions)

        # make the image background transparent
        self.image.fill(Color.BLACK.value)
        self.image.set_colorkey(Color.BLACK.value)

        pygame.draw.rect(
            self.image,
            color,
            (0, 0, side, side)
        )

        self.rect = self.image.get_rect()

        self.rect.x = start_x
        self.rect.y = start_y

        self.velocity_x = choice((-1, 1)) * BALL_SPEED_X
        self.velocity_y = -BALL_SPEED_Y