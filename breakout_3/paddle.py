import pygame
from colors import Color
from constants import PADDLE_SPEED, SCREEN_WIDTH

class Paddle(pygame.sprite.Sprite):
    def move_left(self):
        self.rect.x -= PADDLE_SPEED
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self):
        self.rect.x += PADDLE_SPEED
        limit = SCREEN_WIDTH - self.width
        if self.rect.x > limit:
            self.rect.x = limit

    def __init__(self, color, width, height, start_x, start_y):
        super().__init__()
        self.width = width
        self.height = height

        dimensions = (width, height)

        self.image = pygame.Surface(dimensions)

        # set the image background to be transparent
        self.image.fill(Color.BLACK.value)
        self.image.set_colorkey(Color.BLACK.value)

        pygame.draw.rect(
            self.image,
            color,
            (0, 0, width, height)
        )

        self.rect = self.image.get_rect()

        self.rect.x = start_x
        self.rect.y = start_y