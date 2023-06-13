import pygame
from code.settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../img/textures/rock1.png").convert_alpha()
        self.rectangle = self.image.get_rect(topleft=pos)

