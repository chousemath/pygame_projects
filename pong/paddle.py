import pygame
from colors import WHITE, BLACK
from constants import SCREEN_HEIGHT, PADDLE_HEIGHT


class Paddle(pygame.sprite.Sprite):
    '''
    Template for all paddle sprites
    '''
    def __init__(self, color, width, height, position):
        # call the constructor of the parent class
        super().__init__()

        self.image = pygame.Surface((width, height))
        # set the background color of the paddle
        # make the background transparent
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # draw the paddle
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        # store a reference to the rectangle object
        # that has the dimensions of the image
        self.rect = self.image.get_rect()
        x, y = position
        self.rect.x = x
        self.rect.y = y

    def move_vert(self, pixels):
        '''
        move_vert() takes two arguments.
        The first one is implicit and is called self.
        It refers to the current object.
        The second one is called pixels and refers
        to the number of pixels we will use to move
        the paddle.
        '''
        self.rect.y += pixels
        max_y = SCREEN_HEIGHT - PADDLE_HEIGHT
        if self.rect.y > max_y:
            self.rect.y = max_y
        elif self.rect.y < 0:
            self.rect.y = 0
