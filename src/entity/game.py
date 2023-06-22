import pygame

from src.entity.tile import Tile
from src.entity.player import Player
from src.debug import debug
from src.support import *


class Game:
    def __init__(self):
        # Get Display window (surface)
        self.display_surface = pygame.display.get_surface()

        # Sprite Groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        self.player = None
        self.init_map()

    def init_map(self):
        layouts = {
            'boundary': import_csv_layout(FLOOR_BLOCKS_PATH_CSV),
            'object': import_csv_layout(FLOOR_OBJECTS_PATH_CSV),
        }

        graphics = {
            'objects': import_folder(FLOOR_OBJECTS_PATH)
        }
        # print(graphics['objects'])

        for ob in graphics['objects']:
            print(ob)

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    # Object coordinate is position multiplied by tile-size
                    if col != '-1':
                        x = col_index * TILE_SIZE
                        y = row_index * TILE_SIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacles_sprites], 'invisible')
                        if style == 'object':
                            pass
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacles_sprites], 'object', surf)
                # Deciding by the key symbol create a new displayable object and give him a group
        #         if key == "x":
        #             Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
        #         elif key == "p":
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)
        self.player = Player((450, 2200), [self.visible_sprites], self.obstacles_sprites)

    def run(self, events):
        """
        Update and draw the game.
        :return: None
        """
        self.visible_sprites.custom_draw(self.player)  # draw all visible sprites on screen
        self.visible_sprites.update()  # update all visible sprites on screen
        debug(self.player.direction)
        return self


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load(FLOOR_TEXTURE_PATH).convert()
        self.floor_surf = pygame.transform.scale(self.floor_surf, FLOOR_TEXTURE_SIZE)
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

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

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
