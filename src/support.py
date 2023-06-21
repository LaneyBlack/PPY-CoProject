from src.settings import *
from csv import reader
from os import walk
import pygame
import pathlib

pygame.init()
pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


# print(import_csv_layout("../img/map/map._Objects.csv"))

def import_folder(path):
    surface_list = []


    for _, __, img_files in walk(path):
        i = 0
        for image in img_files:
            check_path = pathlib.Path(path + '/' + image).suffix
            if check_path == '.png':
                full_path = path + '/' + str(i) + '.png'
                i += 1
                print(full_path)
                image_surf = pygame.image.load(full_path).convert_alpha()
                image_surf = pygame.transform.scale(image_surf, PLAYER_TEXTURE_SIZE)
                surface_list.append(image_surf)

    return surface_list


#print(import_folder(FLOOR_OBJECTS_PATH))
