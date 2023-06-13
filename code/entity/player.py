import pygame
from code.settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(PLAYER_TEXTURE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_TEXTURE_SIZE)
        # Creating rectangle to the library (this var name is used by lib)
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        """
        Getting input from the keyboard
        to change direction
        :return: None
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        """
        Player movement
        :param speed: int
            Player speed (default = 5)
        :return: None
        """
        if self.direction.magnitude() != 0:  # the length of the vector
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

        #self.rect.center += self.direction * speed

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
                if sprite.rect.colliderect(self.rect):  # check for collision between sprite and player
                    if self.direction.x > 0:  # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def update(self):
        """
        Update methods
        :return: None
        """
        self.input()
        self.move(self.speed)
