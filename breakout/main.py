from enum import Enum
from time import sleep
import pygame as pyg
from pygame.display import set_mode, set_caption, flip
from pygame.time import Clock
from pygame.draw import line
from pygame.font import Font
from pygame.sprite import Group, collide_mask, spritecollide
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LINE_START,
    LINE_END,
    LINE_WIDTH,
    SCORE_POSITION,
    LIVES_POSITION,
    FRAMERATE,
    BRICK_WIDTH,
    BRICK_HEIGHT,
)
from colors import DARKBLUE, WHITE, LIGHTBLUE, RED, ORANGE, YELLOW
from paddle import Paddle
from ball import Ball
from player import Player
from brick import Brick

pyg.init()

player = Player(score=0, lives=10)

# Open up a new game screen
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = set_mode(size)
set_caption("breakout game")


class GameState(Enum):
    PLAY = 1
    WIN = 2
    LOSE = 3
    QUIT = 4


game_state = GameState.PLAY

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
ball = Ball(
    color=WHITE,
    side=10,
    start_x=350 + 100 / 2 - 10 / 2,
    start_y=560 - 10,
    player=player,
)

# Declare a group that will store all the
# sprites we will create in our game
all_sprites = Group()

# Add the paddle to the list of sprites to
# render
all_sprites.add(paddle)
all_sprites.add(ball)

# Declare another group that will store
# references only to bricks
all_bricks = Group()

# Create brick of various colors and point
# values
BRICK_TOP_OFFSET = 100
for i in range(0, 4):
    x = BRICK_WIDTH + i * (BRICK_WIDTH + 10)
    y = BRICK_TOP_OFFSET
    brick = Brick(RED, BRICK_WIDTH, BRICK_HEIGHT, x, y, 3)
    all_sprites.add(brick)
    all_bricks.add(brick)
for i in range(0, 4):
    x = BRICK_WIDTH + i * (BRICK_WIDTH + 10)
    y = BRICK_TOP_OFFSET + BRICK_HEIGHT + 10
    brick = Brick(ORANGE, BRICK_WIDTH, BRICK_HEIGHT, x, y, 2)
    all_sprites.add(brick)
    all_bricks.add(brick)
for i in range(0, 4):
    x = BRICK_WIDTH + i * (BRICK_WIDTH + 10)
    y = BRICK_TOP_OFFSET + 2 * (BRICK_HEIGHT + 10)
    brick = Brick(YELLOW, BRICK_WIDTH, BRICK_HEIGHT, x, y, 1)
    all_sprites.add(brick)
    all_bricks.add(brick)


while game_state == GameState.PLAY:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            game_state = GameState.QUIT
        elif event.type == pyg.KEYDOWN:
            # The game should exit if the player
            # presses the 'x' key
            if event.key == pyg.K_x:
                game_state = GameState.QUIT

    # Move the paddle when the user
    # uses the left and right arrow keys
    keys = pyg.key.get_pressed()
    if keys[pyg.K_LEFT]:
        paddle.move_left()
    elif keys[pyg.K_RIGHT]:
        paddle.move_right()

    # Main game logic should go here
    all_sprites.update()

    # Handle ball/paddle collision
    if collide_mask(ball, paddle):
        ball.bounce()

    # Handle ball/brick collision
    brick_collisions = spritecollide(ball, all_bricks, False)
    for brick in brick_collisions:
        ball.bounce()
        player.score += brick.points
        brick.kill()

    # Drawing code
    # Clear the screen with dark blue
    screen.fill(DARKBLUE)
    # Draw a divider for your play area and
    # text area
    line(screen, WHITE, LINE_START, LINE_END, LINE_WIDTH)
    # Display the current score
    text = font.render(f"Score: {player.score}", True, WHITE)
    screen.blit(text, SCORE_POSITION)
    # Display the current number of lives
    text = font.render(f"Lives: {player.lives}", True, WHITE)
    screen.blit(text, LIVES_POSITION)

    if len(all_bricks) == 0:
        game_state = GameState.WIN
    elif player.lives <= 0:
        game_state = GameState.LOSE

    # Draw all the sprites in their updated state
    # with a single command
    all_sprites.draw(screen)
    # Update the screen with what we've drawn
    flip()
    # Limit the frame rate to 60fps
    clock.tick(FRAMERATE)

# Now that we are out of the game loop, we can
# assess the current game state and show the
# appropriate message

# If the player has destroyed all the bricks,
# let them know that they have won!
if game_state == GameState.WIN:
    screen.fill(DARKBLUE)
    # The "You win!" message should be a little bit
    # above the center of the screen
    text = font.render("You win!", True, WHITE)
    position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)
    flip()
    sleep(3)

# If the user is out of lives, let them know that
# the game is done
if game_state == GameState.LOSE:
    screen.fill(DARKBLUE)
    # The "Game over" message should be a little bit
    # above the center of the screen
    text = font.render("Game over", True, WHITE)
    position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)
    flip()
    sleep(3)

pyg.quit()
