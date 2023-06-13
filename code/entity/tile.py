import pygame
from code.settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(TILE_TEXTURE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, TILE_TEXTURE_SIZE)
        # Creating rectangle to the library (this var name is used by lib)
        self.rect = self.image.get_rect(topleft=pos)

