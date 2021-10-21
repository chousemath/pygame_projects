import pygame
from colors import Color

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height, start_x, start_y, points):
        super().__init__()
        self.points = points
        dimensions = (width, height)
        self.image = pygame.Surface(dimensions)

        # sets the image background to be transparent
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