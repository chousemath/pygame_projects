from os import path
import pygame as pyg
from color import Color
from random import choices
from string import ascii_uppercase, ascii_lowercase, digits


class Node(pyg.sprite.Sprite):
    def __init__(
        self,
        color=Color.WHITE.value,
        image="eunji-circle.png",
        width=100,
        height=100,
        x=0,
        y=0,
    ):
        super().__init__()
        self.width = width
        self.height = height
        self.key = "".join(choices(ascii_uppercase + ascii_lowercase + digits, k=30))
        self.image_name = image
        self.image = pyg.image.load(path.join("assets", image))
        self.rect = pyg.Rect(x, y, self.width, self.height)
