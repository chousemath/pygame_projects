import pygame as pyg
from pygame.display import set_mode, set_caption, flip
from pygame.time import Clock
from pygame.draw import line
from pygame.font import Font
from pygame.sprite import Group
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LINE_START,
    LINE_END,
    LINE_WIDTH,
    SCORE_POSITION,
    LIVES_POSITION,
    FRAMERATE,
)
from colors import DARKBLUE, WHITE, LIGHTBLUE
from paddle import Paddle
from ball import Ball

pyg.init()

score = 0

lives = 3

# Open up a new game screen
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = set_mode(size)
set_caption("breakout game")
playing = True
# Create a font object to be used
# throughout the game
font = Font(None, 34)
# Create a game clock for limiting the
# frame rate
clock = Clock()

# Create and position our paddle in the
# game screen
# We are 'instantiating' a paddle object
# using the Paddle class
paddle = Paddle(color=WHITE, width=100, height=10, start_x=350, start_y=560)

# Create a ball sprite
game_ball = Ball(color=WHITE, side=10, start_x=350 + 100 / 2 - 10 / 2, start_y=560 - 10)

# Declare  a list called that will store
# all the sprites we will create in our game
all_sprites = Group()

# Add the paddle to the list of sprites to
# render
all_sprites.add(paddle)
all_sprites.add(game_ball)

while playing:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            playing = False
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_x:
                playing = False

    # Move the paddle when the user
    # uses the left and right arrow keys
    keys = pyg.key.get_pressed()
    if keys[pyg.K_LEFT]:
        paddle.move_left()
    elif keys[pyg.K_RIGHT]:
        paddle.move_right()

    # Main game logic should go here
    all_sprites.update()

    # Drawing code
    # Clear the screen with dark blue
    screen.fill(DARKBLUE)
    # Draw a divider for your play area and
    # text area
    line(screen, WHITE, LINE_START, LINE_END, LINE_WIDTH)
    # Display the current score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, SCORE_POSITION)
    text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(text, LIVES_POSITION)
    # Draw all the sprites in their updated state
    # with a single command
    all_sprites.draw(screen)
    # Update the screen with what we've drawn
    flip()
    # Limit the frame rate to 60fps
    clock.tick(FRAMERATE)
pyg.quit()
