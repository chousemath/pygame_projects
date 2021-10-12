import pygame
from pygame import init, QUIT
from pygame.font import Font
from pygame.display import set_caption, set_mode, flip
from pygame.time import Clock
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from snake import Snake
from apple import Apple
from direction import Direction
from colors import BLACK, WHITE

init() # initialize the pygame engine

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = set_mode(size)
set_caption('Snake') # set screen title

clock = Clock()

score = 0
snake = Snake((100, 50))
apples = [Apple(snake) for _ in range(30)]
font = Font(None, 34)

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False
            elif event.key == pygame.K_UP:
                if snake.direction != Direction.DOWN:
                    snake.direction = Direction.UP
            elif event.key == pygame.K_DOWN:
                if snake.direction != Direction.UP:
                    snake.direction = Direction.DOWN
            elif event.key == pygame.K_LEFT:
                if snake.direction != Direction.RIGHT:
                    snake.direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                if snake.direction != Direction.LEFT:
                    snake.direction = Direction.RIGHT

    # Game logic goes here

    # Drawing code goes here
    # Clear the screen with black
    screen.fill(BLACK)
    ok = snake.draw(screen)
    if not ok:
        text = font.render('You lose', True, WHITE)
        position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25)
        text_rect = text.get_rect(center=position)
        screen.blit(text, text_rect)

        text = font.render('Press "x" to quit the game', True, WHITE)
        position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
        text_rect = text.get_rect(center=position)
        screen.blit(text, text_rect)

    for apple in apples:
        collision = apple.draw(screen, snake)
        if collision:
            score += 1

    text = font.render(f'Score: {score}', True, WHITE)
    position = (75, 40)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)

    # Update the screen
    flip()

    # Limit the frame rate to 60 fps
    clock.tick(60)

pygame.quit()


