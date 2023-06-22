import pygame
from src.settings import *
from src.entity.game import Game
from src.pages.login import Login


class Register:
    def __init__(self):
        # Get Display Surface
        self.display_surface = pygame.display.get_surface()
        screen_width = self.display_surface.get_width()
        # Init buttons
        font = pygame.font.Font(FONT_PATH, 90)
        buttons_width = 800
        buttons_height = 100  # px
        buttons_x = (screen_width / 2) - (buttons_width / 2)
        self.buttons = [
            {"coords": [buttons_x, 750, buttons_width, buttons_height],
             "edges": [buttons_x, buttons_x + buttons_width, 750, 750 + buttons_height],
             "text": "Register",
             "text-render": font.render("Register", False, BUTTON_TEXT_COLOR),
             "text-coords": (buttons_x + buttons_width / 3.4, 750)},
        ]
        # Init text boxes
        font = pygame.font.Font(FONT_PATH, 20)
        texbox_width = buttons_width  # px
        textbox_height = 80  # px
        text_boxes_x = buttons_x
        text_boxes_y = [250, 400, 550]
        self.text_boxes = [
            {"name": "Login",
             "text-render": font.render("Login", False, BUTTON_TEXT_COLOR),
             "coords": [text_boxes_x, text_boxes_y[0], texbox_width, textbox_height],
             "edges": [text_boxes_x, text_boxes_x + texbox_width, text_boxes_y[0], text_boxes_y[0] + textbox_height],
             "value": "", },
            {"name": "Password",
             "text-render": font.render("Password", False, BUTTON_TEXT_COLOR),
             "coords": [text_boxes_x, text_boxes_y[1], texbox_width, textbox_height],
             "edges": [text_boxes_x, text_boxes_x + texbox_width, text_boxes_y[1], text_boxes_y[1] + textbox_height],
             "value": "", },
            {"name": "PasswordRepeat",
             "text-render": font.render("Repeat Password", False, BUTTON_TEXT_COLOR),
             "coords": [text_boxes_x, text_boxes_y[2], texbox_width, textbox_height],
             "edges": [text_boxes_x, text_boxes_x + texbox_width, text_boxes_y[2], text_boxes_y[2] + textbox_height],
             "value": "", },
        ]

    def run(self):
        # Get mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.display_surface.fill(BACKGROUND_COLOR)
        for text_box in self.text_boxes:
            pygame.draw.rect(self.display_surface, TEXBOX_COLOR, text_box["coords"],50)
        # ToDo make it in one method
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
