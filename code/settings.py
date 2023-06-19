"""There you can find and change all the project settings"""
# WARING: on Mac it is "../img", on Win it is "img"
IMAGE_FOLDER_PATH = "img" # ../img on Mac and "img" on Win

# ---===--- Main window settings ---===---
GAME_TITLE = "Harry Potter : The Adventures"
GAME_ICON_PATH = IMAGE_FOLDER_PATH + "/icon.png"
WIN_WIDTH = 1640  # px
WIN_HEIGHT = 920  # px
FPS = 60

# ---===--- Texture paths ---===---
PLAYER_TEXTURE_PATH = IMAGE_FOLDER_PATH + "/graphics/cat.png"
PLAYER_TEXTURE_SIZE = (62, 62)
TILE_TEXTURE_PATH = IMAGE_FOLDER_PATH + "/graphics/rock1.png"
TILE_TEXTURE_SIZE = (80, 80)
# ---===--- Map settings ---===---
FLOOR_TEXTURE_PATH = IMAGE_FOLDER_PATH + "/map/floor.png"
FLOOR_TEXTURE_SIZE = (3200, 3200)

FLOOR_BLOCKS_PATH_CSV = IMAGE_FOLDER_PATH + "/map/map._FloorBlocks.csv"

FLOOR_OBJECTS_PATH = IMAGE_FOLDER_PATH + "/map/objects"
FLOOR_OBJECTS_PATH_CSV = IMAGE_FOLDER_PATH + "/map/map._Objects.csv"
TILE_SIZE = 64  # px

# ToDo this is not needed for now
# Currently it's 30x20 (WxH). Here in lists 20 columns and 30 rows
# x - rock, p - player, " " - is empty space
# WARNING! BEWARE! this map is rotated (North is in this direction <---)
WORLDMAP = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " ", " ", "x", " ", " ", "x", " ", " ", "x", "x"],
    ["x", " ", "p", " ", " ", " ", " ", "x", " ", " ", " ", " ", "x", " ", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " ", " ", "x", "x", " ", "x", " ", " ", " ", "x"],
    ["x", "x", "x", " ", " ", "x", "x", "x", "x", "x", "x", " ", "x", " ", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", "x", "x", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", "x", " ", "x", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", " ", "x", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " ", "x", "x"],
    ["x", " ", " ", " ", "x", " ", "x", "x", "x", " ", " ", "x", "x", " ", " ", "x", " ", " ", " ", "x"],
    ["x", " ", "x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x", " ", "x", " ", "x", "x", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x", " ", " ", " ", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", "x", " ", "x", " ", "x", " ", " ", " ", "x", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", "x", " ", " ", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", "x", " ", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", "x", "x", "x", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", "x", "x", " ", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", "x", "x", "x", " ", " ", "x", "x", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", "x", "x", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", "x", "x", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", "x", "x", " ", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", "x", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", "x", " ", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]

# ---===--- Debug settings ---===---
DEBUG_FONT_SIZE = 20
DEBUG_FONT_COLOR = "Red"
