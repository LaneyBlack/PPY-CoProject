import pygame
from src.settings import *
from src.entity.game import Game
from src.pages.login import Login


class Register:
    def __init__(self):
        # Get Display Surface
        self.display_surface = pygame.display.get_surface()
        screen_width = self.display_surface.get_width()
        # Load title
        # Load text boxes
        texbox_width = 800  # px
        textbox_height = 80  # px
        tex_boxes_x = (screen_width / 2) - (texbox_width / 2)
        font = pygame.font.Font(FONT_PATH, 90)
        self.buttons = [
            {"name": "Login",
             "coords": [tex_boxes_x, 450, texbox_width, textbox_height],
             "edges": [tex_boxes_x, tex_boxes_x + texbox_width, 450, 450 + textbox_height], },
            {"name": "Password",
             "coords": [tex_boxes_x, 600, texbox_width, textbox_height],
             "edges": [tex_boxes_x, tex_boxes_x + texbox_width, 600, 600 + textbox_height], },
        ]
        # Load buttons
        buttons_width = texbox_width
        buttons_height = 100  # px
        buttons_x = tex_boxes_x
        self.buttons = [
            {"coords": [buttons_x, 750, buttons_width, buttons_height],
             "edges": [buttons_x, buttons_x + buttons_width, 750, 750 + buttons_height],
             "text": "Register",
             "text-render": font.render("Register", False, BUTTON_TEXT_COLOR),
             "text-coords": (buttons_x + buttons_width / 3.4, 750)},
        ]

    def run(self):
        # Get mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.display_surface.fill(BACKGROUND_COLOR)
        for button in self.buttons:
            if button["edges"][0] <= mouse[0] <= button["edges"][1] and \
                    button["edges"][2] <= mouse[1] <= button["edges"][3]:
                pygame.draw.rect(self.display_surface, BUTTON_ACTIVE_COLOR, button["coords"], 50)
                if click[0]:
                    if button["text"] == "Register":
                        # if logic
                        return Game()
            else:
                pygame.draw.rect(self.display_surface, BUTTON_IDLE_COLOR, button["coords"], 50)
            self.display_surface.blit(button["text-render"], button["text-coords"])
        return self
