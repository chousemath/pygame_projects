import pygame as pyg
from node import Node
from color import Color
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GameState, LevelState

node_list = [
    (100, 100, "eunji-circle.png"),
    (200, 100, "eunji-triangle.png"),
    (300, 100, "eunji-star.png"),
    (400, 100, "eunji-square.png"),
]

nodes = pyg.sprite.Group()
for x, y, im in node_list:
    n = Node(x=x, y=y, image=im)
    nodes.add(n)


class Game:
    def __init__(self):
        dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen = pyg.display.set_mode(dimensions)
        pyg.display.set_caption("Love you!")
        self.clock = pyg.time.Clock()
        self.fps = 60
        self.state = GameState.START_MENU

    def run(self):
        pyg.init()
        self.font = pyg.font.Font(None, 40)
        while self.state != GameState.QUIT:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.state = GameState.QUIT

            mouse_x, mouse_y = pyg.mouse.get_pos()
            nodes.update()

            self.screen.fill(Color.WHITE.value)

            nodes.draw(self.screen)

            mouse_text = f"mouse x: {mouse_x}, mouse_y: {mouse_y}"
            mouse_text = self.font.render(mouse_text, True, Color.BLACK.value)
            position = (SCREEN_WIDTH - 400, SCREEN_HEIGHT - 50)
            self.screen.blit(mouse_text, position)

            pyg.display.flip()

            self.clock.tick(self.fps)

        pyg.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
