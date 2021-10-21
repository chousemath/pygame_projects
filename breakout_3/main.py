import pygame
from enum import Enum
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FRAMERATE,
    BALL_SIDE,
    PADDLE_WIDTH,
    BRICK_WIDTH,
    BRICK_HEIGHT,
    BRICK_TOP_OFFSET,
    BRICK_SIDE_OFFSET,
)
from colors import Color
from paddle import Paddle
from ball import Ball
from brick import Brick

class GameState(Enum):
    PLAY = 1
    WIN = 2
    LOSE = 3
    QUIT = 4

game_state = GameState.PLAY

pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('BREAKOUT!')
clock = pygame.time.Clock()

paddle = Paddle(
    color=Color.WHITE.value,
    width=PADDLE_WIDTH,
    height=10,
    start_x=350,
    start_y=560
)
ball = Ball(
    color=Color.WHITE.value,
    side=BALL_SIDE,
    start_x=350 + PADDLE_WIDTH / 2 - BALL_SIDE / 2,
    start_y=560 - BALL_SIDE
)

sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

sprites.add(paddle)
sprites.add(ball)

for i in range(0, 4):
    start_x = BRICK_WIDTH + i * (BRICK_WIDTH + BRICK_SIDE_OFFSET)
    start_y = BRICK_TOP_OFFSET
    brick = Brick(
        color=Color.ORANGE.value,
        width=BRICK_WIDTH,
        height=BRICK_HEIGHT,
        start_x=start_x,
        start_y=start_y,
        points=3
    )
    sprites.add(brick)
    bricks.add(brick)

for i in range(0, 4):
    start_x = BRICK_WIDTH + i * (BRICK_WIDTH + BRICK_SIDE_OFFSET)
    start_y = BRICK_TOP_OFFSET + BRICK_HEIGHT + BRICK_SIDE_OFFSET
    brick = Brick(
        color=Color.RED.value,
        width=BRICK_WIDTH,
        height=BRICK_HEIGHT,
        start_x=start_x,
        start_y=start_y,
        points=2
    )
    sprites.add(brick)
    bricks.add(brick)

for i in range(0, 4):
    start_x = BRICK_WIDTH + i * (BRICK_WIDTH + BRICK_SIDE_OFFSET)
    start_y = BRICK_TOP_OFFSET + 2 * (BRICK_HEIGHT + BRICK_SIDE_OFFSET)
    brick = Brick(
        color=Color.YELLOW.value,
        width=BRICK_WIDTH,
        height=BRICK_HEIGHT,
        start_x=start_x,
        start_y=start_y,
        points=1
    )
    sprites.add(brick)
    bricks.add(brick)

while game_state == GameState.PLAY:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = GameState.QUIT
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_state = GameState.QUIT

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.move_left()
    elif keys[pygame.K_RIGHT]:
        paddle.move_right()

    if pygame.sprite.collide_mask(ball, paddle):
        ball.bounce()

    collided_bricks = pygame.sprite.spritecollide(ball, bricks, False)
    for brick in collided_bricks:
        ball.bounce()
        brick.kill()

    sprites.update()

    screen.fill(Color.DARKBLUE.value)

    sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FRAMERATE)

pygame.quit()

