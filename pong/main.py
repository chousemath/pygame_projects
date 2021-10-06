import pygame  # Import the pygame library
from paddle import Paddle
from colors import WHITE, BLACK
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH,
                       PADDLE_HEIGHT, SPEED)

# Define your window size
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
# Initialize the game engine
pygame.init()
# Create a new screen object
screen = pygame.display.set_mode(size)
# Set the title of the game
pygame.display.set_caption("Pong")

# Game loop will continue until the user
# exits the game
playing = True

# The clock controls how fast
# the screen updates
clock = pygame.time.Clock()

# instantiate our paddles
position_a = (20, 200)
position_b = (670, 200)
paddle_a = Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT, position_a)
paddle_b = Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT, position_b)

# instantiate our sprite group
all_sprites = pygame.sprite.Group()
# add the paddles to the list of sprites
all_sprites.add(paddle_a)
all_sprites.add(paddle_b)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # Let’s add four event handlers to move
    # the paddle up or down
    keys = pygame.key.get_pressed()
    # when the players press the W or S keys (Paddle A)
    if keys[pygame.K_w]:
        paddle_a.move_vert(-SPEED)
    if keys[pygame.K_s]:
        paddle_a.move_vert(SPEED)
    # or the up and down arrow keys (paddle B)
    if keys[pygame.K_UP]:
        paddle_b.move_vert(-SPEED)
    if keys[pygame.K_DOWN]:
        paddle_b.move_vert(SPEED)
    # use the "x" key as a quit button
    if keys[pygame.K_x]:
        playing = False

    # Game logic belongs here
    all_sprites.update()

    # Drawing code goes here
    # Clear the screen to black.
    screen.fill(BLACK)
    # Draw the "net"
    line_start = (SCREEN_WIDTH // 2, 0)
    line_end = (SCREEN_WIDTH // 2, SCREEN_HEIGHT)
    line_width = 5
    pygame.draw.line(screen, WHITE, line_start, line_end, line_width)

    # draw all of the sprites
    all_sprites.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Limit frame rate to 60fps
    clock.tick(60)

pygame.quit()
