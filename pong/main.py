import pygame  # Import the pygame library
from pygame.sprite import collide_mask
from paddle import Paddle
from ball import Ball
from colors import WHITE, BLACK
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH,
                       PADDLE_HEIGHT, BALL_WIDTH, BALL_HEIGHT, PADDLE_SPEED,
                       FONT_SIZE, SCORE_LEFT, SCORE_RIGHT)

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

# instantiate our ball(s)
position_ball = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
ball_1 = Ball(WHITE, BALL_WIDTH, BALL_HEIGHT, position_ball)
UPPER_LIMIT_X = SCREEN_WIDTH - BALL_WIDTH
UPPER_LIMIT_Y = SCREEN_HEIGHT - BALL_HEIGHT

# instantiate our sprite group
all_sprites = pygame.sprite.Group()
# add the paddles to the list of sprites
all_sprites.add(paddle_a)
all_sprites.add(paddle_b)
all_sprites.add(ball_1)

# create a font object
FONT = pygame.font.Font(None, FONT_SIZE)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # Let’s add four event handlers to move
    # the paddle up or down
    keys = pygame.key.get_pressed()
    # when the players press the W or S keys (Paddle A)
    if keys[pygame.K_w]:
        paddle_a.move_vert(-PADDLE_SPEED)
    if keys[pygame.K_s]:
        paddle_a.move_vert(PADDLE_SPEED)
    # or the up and down arrow keys (paddle B)
    if keys[pygame.K_UP]:
        paddle_b.move_vert(-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        paddle_b.move_vert(PADDLE_SPEED)
    # use the "x" key as a quit button
    if keys[pygame.K_x]:
        playing = False

    # Check if the ball_1 has collided with the
    # left or right walls
    if ball_1.rect.x <= 0:
        paddle_a.score += 1
        ball_1.velocity.x = -ball_1.velocity.x
    elif ball_1.rect.x >= UPPER_LIMIT_X:
        paddle_b.score += 1
        ball_1.velocity.x = -ball_1.velocity.x

    # Check if the ball_1 has collided with the
    # top or bottom walls
    if ball_1.rect.y <= 0:
        ball_1.velocity.y = -ball_1.velocity.y
    elif ball_1.rect.y >= UPPER_LIMIT_Y:
        ball_1.velocity.y = -ball_1.velocity.y

    # handle paddle / ball_1 collision
    if collide_mask(ball_1, paddle_a) or collide_mask(ball_1, paddle_b):
        ball_1.bounce()

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

    # Display scores
    score_text = FONT.render(str(paddle_a.score), 1, WHITE)
    screen.blit(score_text, SCORE_LEFT)
    score_text = FONT.render(str(paddle_b.score), 1, WHITE)
    screen.blit(score_text, SCORE_RIGHT)

    # Update the screen
    pygame.display.flip()

    # Limit frame rate to 60fps
    clock.tick(60)

pygame.quit()
