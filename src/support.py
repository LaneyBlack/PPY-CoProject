from src.settings import *
from csv import reader
from os import walk
import pygame
import pathlib

pygame.init()
pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


def import_csv_layout(path):
    """
    The function imports data from a CSV file specified by path
    and creates a two-dimensional terrain map.
    :param path: str
        Path to the CSV file containing the terrain layout.
    :return: list
        A two-dimensional list representing the terrain layout.
    """
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    """
    The function is used to import a set of images from a specified folder
    and create a list of surfaces for each image.
    :param path: str
        The path to the folder containing the images.
    :return: list
        A list of surfaces for each image.
    """
    surface_list = []

    for _, __, img_files in walk(path):
        i = 0
        for image in img_files:
            check_path = pathlib.Path(path + '/' + image).suffix
            if check_path == '.png':
                full_path = path + '/' + str(i) + '.png'
                i += 1
                image_surf = pygame.image.load(full_path).convert_alpha()
                image_surf = pygame.transform.scale(image_surf, PLAYER_TEXTURE_SIZE)
                surface_list.append(image_surf)

    return surface_list
