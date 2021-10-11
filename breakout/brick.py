from pygame.sprite import Sprite
from pygame import Surface
from pygame.draw import rect
from colors import BLACK


class Brick(Sprite):
    def __init__(self, color, width, height, x, y, points):
        super().__init__()
        self.points = points
        dimensions = (width, height)
        # Create a Pygame "surface" for the brick
        # to be drawn into, and...
        self.image = Surface(dimensions)
        # ...make the background transparent
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw a rectangle around the surface
        placement = (0, 0, width, height)
        rect(self.image, color, placement)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
