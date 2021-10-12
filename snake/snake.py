from direction import Direction
from pygame import Rect
from pygame.draw import rect
from colors import GREEN
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Snake:
    side = 10
    def __init__(self, start_pos):
        self.direction = Direction.RIGHT
        self.body = [
            start_pos,
            (start_pos[0] - 1 * self.side, start_pos[1]),
            (start_pos[0] - 2 * self.side, start_pos[1]),
            (start_pos[0] - 3 * self.side, start_pos[1]),
            (start_pos[0] - 4 * self.side, start_pos[1]),
        ]
        self.positions = {pos: True for pos in self.body}

    def draw(self, screen):
        if not self.body:
            return False

        for i in range(len(self.body) - 2, -1, -1):
            self.body[i+1] = self.body[i]
        x = y = 0

        if self.direction == Direction.UP:
            y -= self.side
        elif self.direction == Direction.DOWN:
            y += self.side

        if self.direction == Direction.LEFT:
            x -= self.side
        elif self.direction == Direction.RIGHT:
            x += self.side

        new_head = (self.body[0][0] + x, self.body[0][1] + y)

        if new_head in self.body or new_head[0] < 0 or new_head[0] > SCREEN_WIDTH - self.side or new_head[1] < 0 or new_head[1] > SCREEN_HEIGHT - self.side:
            self.body.clear()
            return False

        self.body[0] = new_head

        for pos in self.body:
            self.positions[pos] = True
            rect(screen, GREEN, Rect(pos[0], pos[1], self.side, self.side))

        return True

    def extend(self):
        self.body.append(self.body[-1])
