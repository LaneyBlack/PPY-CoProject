import pygame
from settings import *

pygame.init()
font = pygame.font.Font(None, DEBUG_FONT_SIZE)


def debug(info, y=10, x=10):
    """
    Method for showing reports on screen
    :param info: string
        Text to show on screen
    :param y: int
        Y Coordinate of the infobox (default = 10)
    :param x: int
        X Coordinate of the infobox (default = 10)
    :return:
    """
    display_surface = pygame.display.get_surface()
    debug_info = font.render(str(info), True, DEBUG_FONT_COLOR)
    debug_rect = debug_info.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_info, debug_rect)
