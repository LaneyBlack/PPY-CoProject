import pygame
from src.settings import *


class Login:
    def __init__(self):
        # Get Display Surface
        self.display_surface = pygame.display.get_surface()
        screen_width = self.display_surface.get_width()

    def run(self,events):
        return self
