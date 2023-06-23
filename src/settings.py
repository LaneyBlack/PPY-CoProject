"""
Project Settings
"""

# WARNING: There is two options for image folder 1)"../assets" 2) "assets"
ASSETS_FOLDER_PATH = "../assets"
IMAGE_FOLDER_PATH = ASSETS_FOLDER_PATH + "/img"  # <-------WARNING

# DB_STRING = "postgresql://s24382:s24382@212.182.24.105:15432/s24382"  # postgres sql
DB_STRING = "sqlite:///db/project.db"  # sqlite

# ---===--- Main window settings ---===---
GAME_TITLE = "Cat Farm : Island"
GAME_ICON_PATH = IMAGE_FOLDER_PATH + "/icon.png"
FONT_PATH = ASSETS_FOLDER_PATH + "/VT323-Regular.ttf"
WIN_WIDTH = 1640  # px
WIN_HEIGHT = 920  # px
FPS = 60

# ---===--- Window Colors ---===---
BACKGROUND_COLOR = (118, 161, 87)

TITLE_COLOR = (233, 227, 117)

BUTTON_IDLE_COLOR = (215, 158, 95)
BUTTON_ACTIVE_COLOR = (239, 186, 117)
BUTTON_TEXT_COLOR = (0, 0, 0)

TEXBOX_COLOR = (193, 199, 187)
TEXBOX_ACTIVE_COLOR = (221, 223, 210)
TEXBOX_TEXT_COLOR = (129, 139, 133)
TEXBOX_VALUE_COLOR = (0, 0, 0)

ERROR_MESSAGE_COLOR = (160, 50, 50)

# ---===--- Texture paths ---===---
PLAYER_TEXTURE_PATH = IMAGE_FOLDER_PATH + "/graphics/cat.png"
PLAYER_TEXTURE_SIZE = (62, 62)

PLAYER_ANIMATIONS_PATH = IMAGE_FOLDER_PATH + "/animations/"

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
