import pygame
from random import randint
from colors import BLACK
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Velocity:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ball(pygame.sprite.Sprite):
    '''
    Represents a ball, derived from the "Sprite" class
    '''
    def __init__(self, color, width, height, position):
        # call the constructor of the parent class
        super().__init__()
        # Pass in the color of the ball, its width and height.
        self.width = width
        self.height = height
        DIMENSIONS = (width, height)
        self.image = pygame.Surface(DIMENSIONS)
        # Set the background color and set it to be transparent
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the "ball" (actually a rectangle)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        # Set the initial velocity of the ball
        velocity_x = 9
        velocity_y = randint(-8, 8)
        self.velocity = Velocity(x=velocity_x, y=velocity_y)
        # Fetch the rectangle object that has the same
        # dimensions of the image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def bounce(self):
        self.velocity.x = -self.velocity.x
        self.velocity.y = randint(-8, 8)
