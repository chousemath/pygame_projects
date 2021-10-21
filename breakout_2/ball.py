import pygame
from colors import Color
from random import choice
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SPEED_X, BALL_SPEED_Y


class Ball(pygame.sprite.Sprite):
    def bounce(self):
        # make sure ball is outside of the collision
        # zone of the paddle
        self.rect.x -= self.velocity_x
        self.rect.y -= self.velocity_y
        # reverse the y-velocity of the ball
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

        self.image.fill(Color.BLACK.value)
        self.image.set_colorkey(Color.BLACK.value)

        pygame.draw.rect(self.image, color, (0, 0, side, side))

        self.rect = self.image.get_rect()

        self.rect.x = start_x
        self.rect.y = start_y

        self.velocity_x = choice([-1, 1]) * BALL_SPEED_X
        self.velocity_y = -BALL_SPEED_Y
