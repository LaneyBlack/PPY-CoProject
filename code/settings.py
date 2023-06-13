"""There you can find and change all the project settings"""

# ---===--- Main window settings ---===---
GAME_TITLE = "Harry Potter : The Adventures"
GAME_ICON_PATH = "img/icon.png"
WIN_WIDTH = 1640  # px
WIN_HEIGHT = 920  # px
FPS = 60

# ---===--- Texture paths ---===---
PLAYER_TEXTURE_PATH = "img/textures/hero.png"
PLAYER_TEXTURE_SIZE = (80, 100)
TILE_TEXTURE_PATH = "img/textures/rock1.png"
TILE_TEXTURE_SIZE = (80, 80)
# ---===--- Map settings ---===---
TILE_SIZE = 64  # px
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
