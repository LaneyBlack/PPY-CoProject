import pygame
from src.settings import *
from src.support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, create_water, destroy_watering_can):
        super().__init__(groups)
        self.image = pygame.image.load(PLAYER_TEXTURE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_TEXTURE_SIZE)
        # Creating rectangle to the library (this var name is used by lib)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        # graphics setup
        self.import_player_assets()
        self.status = "down"
        self.frame_index = 0
        self.animation_speed = 0.05

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.gardening = False
        self.gardening_cooldown = 400
        self.gardening_time = None

        self.obstacle_sprites = obstacle_sprites

        # garden
        self.create_water = create_water
        self.destroy_watering_can = destroy_watering_can
        self.bailer_index = 0
        #self.watering_cans =

    def import_player_assets(self):
        self.animations = {"up": [], "down": [], "left": [], "right": [], "right_idle": [],
                           "left_idle": [], "up_idle": [], "down_idle": [], "right_water": [],
                           "left_water": [], "up_water": [], "down_water": []}

        for animation in self.animations.keys():
            full_path = PLAYER_ANIMATIONS_PATH + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        """
        Getting input from the keyboard
        to change direction
        :return: None
        """
        if not self.gardening:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.direction.y = -1
                self.status = "up"
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.direction.y = 1
                self.status = "down"
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction.x = 1
                self.status = "right"
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction.x = -1
                self.status = "left"
            else:
                self.direction.x = 0

            # interaction with plants
            if keys[pygame.K_f] and not self.gardening:
                self.gardening = True
                self.gardening_time = pygame.time.get_ticks()
                self.create_water()

    def move(self, speed):
        """
        Player movement
        :param speed: int
            Player speed (default = 5)
        :return: None
        """
        if self.direction.magnitude() != 0:  # the length of the vector
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

        # self.rect.center += self.direction * speed

    def collision(self, direction):
        """
        Does not allow for a collision
        between player and sprite
        :param direction: string
            Player direction (horizontal or vertical)
        :return: None
        """
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):  # check for collision between sprite and player
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.gardening:
            if current_time - self.gardening_time >= self.gardening_cooldown:
                self.gardening = False
                self.destroy_watering_can()

    def get_status(self):

        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not "idle" in self.status and not "water" in self.status:
                self.status = self.status + "_idle"

        if self.gardening:
            self.direction.x = 0
            self.direction.y = 0
            if not "water" in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle", "_water")
                else:
                    self.status = self.status + "_water"

        else:
            if "water" in self.status:
                self.status = self.status.replace("_water", "")

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        """
        Update methods
        :return: None
        """
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
