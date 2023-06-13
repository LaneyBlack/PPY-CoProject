import pygame
from code.settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../img/hero.png").convert_alpha()
        self.rectangle = self.image.get_rect(topleft=pos)