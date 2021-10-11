from pygame import Surface
from pygame.sprite import Sprite
from pygame.draw import rect
from colors import BLACK
from constants import PADDLE_SPEED, SCREEN_WIDTH


class Paddle(Sprite):
    def __init__(self, color, width, height, start_x=0, start_y=0):
        # Call the parent class constructor
        super().__init__()
        self.width = width
        self.height = height
        dimensions = (width, height)
        self.image = Surface(dimensions)
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the paddle rectangle over the image
        rect(self.image, color, (0, 0, width, height))
        # Fetch and store the rectangular object
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def move_left(self):
        self.rect.x -= PADDLE_SPEED
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self):
        self.rect.x += PADDLE_SPEED
        limit = SCREEN_WIDTH - self.width
        if self.rect.x > limit:
            self.rect.x = limit
