import pygame

from src.entity.tile import Tile
from src.entity.player import Player
from src.debug import debug
from src.support import *
from src.entity.watering_can import WateringCan


class Game:
    def __init__(self):
        """
        Represents the game instance.

        The Game class initializes the game, sets up the display surface and creates sprite groups.
        It also initializes the game map and the player object.

        Attributes:
            display_surface (pygame.Surface): The game's display surface.
            visible_sprites (YSortCameraGroup): Sprite group for visible sprites.
            obstacles_sprites (pygame.sprite.Group): Sprite group for obstacle sprites.
            player (Player): The player object.
        """
        # Get Display window (surface)
        self.display_surface = pygame.display.get_surface()

        # Sprite Groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        self.player = None
        self.init_map()

    def init_map(self):
        """
        Initializes the game map by loading layouts and graphics.

        The method loads layout data from CSV files and graphics data from folders.
        It iterates over the layout and creates tiles and objects based on the values in the layout.

        :return:
        """
        layouts = {
            'boundary': import_csv_layout(FLOOR_BLOCKS_PATH_CSV),
            'object': import_csv_layout(FLOOR_OBJECTS_PATH_CSV),
        }

        graphics = {
            'objects': import_folder(FLOOR_OBJECTS_PATH)
        }


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
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacles_sprites], 'object', surf)
                # Deciding by the key symbol create a new displayable object and give him a group
        #         if key == "x":
        #             Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
        #         elif key == "p":
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)
        self.player = Player((450, 2200), [self.visible_sprites], self.obstacles_sprites, self.create_water, self.destroy_watering_can)

    def create_water(self):
        """
        Creates a watering can object.
        Creates a watering can object and adds it to the visible sprites group.

        :return:
        """
        self.current_watering_can = WateringCan(self.player,[self.visible_sprites])

    def destroy_watering_can(self):
        """
        Destroys the current watering can object.
        Removes the current watering can object from the visible sprites group.

        :return:
        """
        if self.current_watering_can:
            self.current_watering_can.kill()
        self.current_watering_can = None


    def run(self, events):
        """
        Updates and draws the game.

        This method is called in the game loop to update and draw the game state.
        It updates the visible sprites, handles player status and direction, and returns the updated game instance.

        :param events:list: list of pygame window events
        :return: self: The updated game instance.
        """
        self.visible_sprites.custom_draw(self.player)  # draw all visible sprites on screen
        self.visible_sprites.update()  # update all visible sprites on screen
        return self


class YSortCameraGroup(pygame.sprite.Group):
    """
    Represents a custom sprite group for camera offset.

    The YSortCameraGroup class extends the pygame.sprite.Group class to provide
    additional functionality for camera offset. It also handles drawing the floor.

    Attributes:
        display_surface (pygame.Surface): The game's display surface.
        half_width (int): Half the width of the display surface.
        half_height (int): Half the height of the display surface.
        offset (pygame.math.Vector2): The camera offset vector.
        floor_surf (pygame.Surface): The floor surface.
        floor_rect (pygame.Rect): The floor rectangle.
    """
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
        Draws sprites on the screen with camera offset.

        This method is responsible for drawing the sprites on the screen with camera offset.
        It calculates the offset based on the player's position and draws the sprites accordingly.
        It also draws the floor surface.

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
