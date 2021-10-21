from enum import Enum
import pygame
from colors import Color
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE, BRICK_WIDTH, BRICK_HEIGHT
from paddle import Paddle
from ball import Ball
from brick import Brick


class GameState(Enum):
    PLAY = 1
    WIN = 2
    LOSE = 3
    QUIT = 4


pygame.init()

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("BREAKOUT!!!")

game_state = GameState.PLAY

clock = pygame.time.Clock()

paddle = Paddle(color=Color.WHITE.value, width=100, height=10, start_x=350, start_y=560)
ball = Ball(
    color=Color.WHITE.value,
    side=10,
    start_x=int(SCREEN_WIDTH / 2 - 5),
    start_y=560 - 10,
)


sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

sprites.add(paddle)
sprites.add(ball)

X_OFFSET = 10
BRICK_TOP_OFFSET = 100

for i in range(0, 4):
    x = BRICK_WIDTH + i * (BRICK_WIDTH + X_OFFSET)
    y = BRICK_TOP_OFFSET
    brick = Brick(
        color=Color.RED.value,
        width=BRICK_WIDTH,
        height=BRICK_HEIGHT,
        start_x=x,
        start_y=y,
        points=1,
    )
    sprites.add(brick)
    bricks.add(brick)

for i in range(0, 4):
    x = BRICK_WIDTH + i * (BRICK_WIDTH + X_OFFSET)
    y = BRICK_TOP_OFFSET + BRICK_HEIGHT + 10
    brick = Brick(
        color=Color.ORANGE.value,
        width=BRICK_WIDTH,
        height=BRICK_HEIGHT,
        start_x=x,
        start_y=y,
        points=2,
    )
    sprites.add(brick)
    bricks.add(brick)

for i in range(0, 4):
    x = BRICK_WIDTH + i * (BRICK_WIDTH + X_OFFSET)
    y = BRICK_TOP_OFFSET + 2*(BRICK_HEIGHT + 10)
    brick = Brick(
        color=Color.YELLOW.value,
        width=BRICK_WIDTH,
        height=BRICK_HEIGHT,
        start_x=x,
        start_y=y,
        points=3,
    )
    sprites.add(brick)
    bricks.add(brick)

while game_state == GameState.PLAY:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = GameState.QUIT

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.move_left()
    elif keys[pygame.K_RIGHT]:
        paddle.move_right()
    elif keys[pygame.K_x]:
        game_state = GameState.QUIT

    # update the state of all of our sprites
    sprites.update()

    if pygame.sprite.collide_mask(ball, paddle):
        ball.bounce()

    brick_collisions = pygame.sprite.spritecollide(ball, bricks, False)
    for brick in brick_collisions:
        ball.bounce()
        brick.kill()

    screen.fill(Color.DARKBLUE.value)

    sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FRAMERATE)

pygame.quit()
