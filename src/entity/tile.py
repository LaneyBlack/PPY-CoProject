import pygame
from src.settings import *


class Tile(pygame.sprite.Sprite):
    """Represents a tile object in the game world."""
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILE_SIZE, TILE_SIZE))):
        """
        Initializes the Tile object.

        Args:
            pos (tuple): The position of the tile (x, y).
            groups (list): The groups to which the tile sprite belongs.
            sprite_type (str): The type of the tile sprite.
            surface (pygame.Surface, optional): The surface representing the tile's image. Defaults to a blank surface with the size of TILE_SIZE.
        """
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -30)
