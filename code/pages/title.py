import pygame
from code.settings import *


class Title:
    def __init__(self):
        # Get Display Surface
        self.display_surface = pygame.display.get_surface()
        # Load title
        self.title = pygame.image.load(BUTTON_IMAGES_PATH + "/reset.png")
        # Load button images and then load buttons
        self.login_button = pygame.image.load(BUTTON_IMAGES_PATH + "/login.png")
        self.register_button = pygame.image.load(BUTTON_IMAGES_PATH + "/reset.png")

    def run(self):
        width = self.display_surface.get_width()
        height = self.display_surface.get_height()
        mouse = pygame.mouse.get_pos()

        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(self.display_surface, "green", [width / 2, height / 2, 140, 40])

        else:
            pygame.draw.rect(self.display_surface, "darkgreen", [width / 2, height / 2, 140, 40])
