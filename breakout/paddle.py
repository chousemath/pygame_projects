from pygame import Surface
from pygame.sprite import Sprite
from pygame.draw import rect
from colors import BLACK


class Paddle(Sprite):
    def __init__(self, color, width, height):
        # Call the parent class constructor
        super().__init__()
        dimensions = (width, height)
        self.image = Surface(dimensions)
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the paddle
        rect(self.image, color, (0, 0, width, height))
        # Fetch and store the rectangular object
        self.rect = self.image.get_rect()
