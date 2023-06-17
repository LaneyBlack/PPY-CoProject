import pygame

from code.entity.tile import Tile
from code.entity.player import Player
from code.settings import *
from code.debug import debug


class Level:
    def __init__(self):
        # Get Display window (surface)
        self.display_surface = pygame.display.get_surface()

        # Sprite Groups
        self.visible_sprites = YSortCameraGroup()
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
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif key == "p":
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

    def run(self):
        """
        Update and draw the game.
        :return: None
        """
        self.visible_sprites.custom_draw(self.player)  # draw all visible sprites on screen
        self.visible_sprites.update()  # update all visible sprites on screen
        debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        """
        Method for drawing sprites on the screen with camera offset.
        :param player: Object representing the player,
            whose position will be used to calculate the offset.
        :return: None
        """

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)