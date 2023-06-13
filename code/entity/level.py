import pygame
from code.settings import *

class Level:
    def __init__(self):
        # Get Display window (surface)
        self.display_surface = pygame.display.get_surface()

        # Sprite Groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.init_map()

    def init_map(self):
        for i, row in enumerate(WORLDMAP):
            for j, col in enumerate(row):
                print(i,j,row)

    def run(self):
        # Update and Draw
        pass