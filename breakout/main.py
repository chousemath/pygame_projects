import pygame as pyg
from pygame.display import set_mode, set_caption, flip
from pygame.time import Clock
from pygame.draw import line
from pygame.font import Font
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
from colors import DARKBLUE, WHITE

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
while playing:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            playing = False
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
    # Update the screen with what we've drawn
    flip()
    # Limit the frame rate to 60fps
    clock.tick(FRAMERATE)
pyg.quit()
