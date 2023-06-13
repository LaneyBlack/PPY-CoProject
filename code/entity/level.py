import pygame

from code.entity.tile import Tile
from code.entity.player import Player
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
            for j, key in enumerate(row):
                # Object coordinate is position multiplied by tile-size
                x = i * TILE_SIZE
                y = j * TILE_SIZE
                # Deciding by the key symbol create a new displayable object and give him a group
                if key == "x":
                    Tile((x,y),[self.visible_sprites, self.obstacles_sprites])
                elif key == "p":
                    Player((x,y),[self.visible_sprites])

    def run(self):
        # Update and Draw
        self.visible_sprites.draw(self.display_surface) # draw all visible sprites on screen