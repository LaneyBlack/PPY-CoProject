import pygame
import src.db.db_service as db_service
from src.db.user import User, password_encode
from src.settings import *
from src.entity.game import Game
from src.debug import *


class Register:
    """
    A class that handles the registration process and user interface for registration.

    Attributes:
        display_surface (pygame.Surface): The display surface to render the UI elements.
        error_message (str): Error message to display if there are any registration errors.
        error_font (pygame.font.Font): Font used for rendering the error message.
        error_message_coords (tuple): Coordinates for rendering the error message.
        buttons (list): List of dictionaries representing the buttons for registration.
        text_boxes (list): List of dictionaries representing the text boxes for input.
        active_text_box_name (str): Name of the currently active text box.
        text_box_font (pygame.font.Font): Font used for rendering the text box values.

    Methods:
        run(events): Runs the registration process and handles user input.

    """

    def __init__(self):
        """
        Initializes the Register class.
        """
        # Get Display Surface
        self.display_surface = pygame.display.get_surface()
        screen_width = self.display_surface.get_width()
        self.error_message = ""
        self.error_font = pygame.font.Font(FONT_PATH, 40)
        self.error_message_coords = (100, 100)
        # Init buttons
        my_font = pygame.font.Font(FONT_PATH, 90)
        buttons_width = 800
        buttons_height = 100  # px
        buttons_x = (screen_width / 2) - (buttons_width / 2)
        self.buttons = [
            {"coords": [buttons_x, 750, buttons_width, buttons_height],
             "edges": [buttons_x, buttons_x + buttons_width, 750, 750 + buttons_height],
             "text": "Register",
             "text-render": my_font.render("Register", False, BUTTON_TEXT_COLOR),
             "text-coords": (buttons_x + buttons_width / 3.4, 750)},
        ]
        # Init text boxes
        my_font = pygame.font.Font(FONT_PATH, 20)
        texbox_width = buttons_width  # px
        textbox_height = 80  # px
        text_boxes_x = buttons_x
        text_boxes_y = [250, 400, 550]
        self.text_boxes = [
            {"name": "Login",
             "type": "Login",
             "text-render": my_font.render("Login", False, TEXBOX_TEXT_COLOR),
             "coords": [text_boxes_x, text_boxes_y[0], texbox_width, textbox_height],
             "edges": [text_boxes_x, text_boxes_x + texbox_width, text_boxes_y[0], text_boxes_y[0] + textbox_height],
             "value": "", },
            {"name": "Password",
             "type": "Password",
             "text-render": my_font.render("Password", False, TEXBOX_TEXT_COLOR),
             "coords": [text_boxes_x, text_boxes_y[1], texbox_width, textbox_height],
             "edges": [text_boxes_x, text_boxes_x + texbox_width, text_boxes_y[1], text_boxes_y[1] + textbox_height],
             "value": "", },
            {"name": "PasswordRepeat",
             "type": "Password",
             "text-render": my_font.render("Repeat Password", False, TEXBOX_TEXT_COLOR),
             "coords": [text_boxes_x, text_boxes_y[2], texbox_width, textbox_height],
             "edges": [text_boxes_x, text_boxes_x + texbox_width, text_boxes_y[2], text_boxes_y[2] + textbox_height],
             "value": "", },
        ]
        self.active_text_box_name = "None"
        self.text_box_font = pygame.font.Font(FONT_PATH, 80)

    def run(self, events):
        """
        Runs the registration process and handles user input.

        Args:
            events (list): List of pygame events to process.

        Returns:
            Game: An instance of the Game class if the registration is successful,
                or self otherwise.
        """
        # Get mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.display_surface.fill(BACKGROUND_COLOR)
        # Draw every text box
        for text_box in self.text_boxes:
            # Different colors for active and not
            if self.active_text_box_name == text_box["name"]:
                rect = pygame.draw.rect(self.display_surface, TEXBOX_ACTIVE_COLOR, text_box["coords"], 50)
            else:
                rect = pygame.draw.rect(self.display_surface, TEXBOX_COLOR, text_box["coords"], 50)
            # Text box name
            self.display_surface.blit(text_box["text-render"], rect)
            # Text box value
            if text_box["type"] == "Password":
                render = self.text_box_font.render("*" * len(text_box["value"]), False, TEXBOX_VALUE_COLOR)
            else:
                render = self.text_box_font.render(text_box["value"], False, TEXBOX_VALUE_COLOR)
            self.display_surface.blit(render, rect)
            # Run through every event
            if self.active_text_box_name == "None" or self.active_text_box_name == text_box["name"]:
                if click[0]:
                    if text_box["edges"][0] <= mouse[0] <= text_box["edges"][1] and \
                            text_box["edges"][2] <= mouse[1] <= text_box["edges"][3]:
                        self.active_text_box_name = text_box["name"]
                    else:
                        self.active_text_box_name = "None"
                # If textbox is active listen to the inputs
                if self.active_text_box_name == text_box["name"]:
                    for event in events:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                text_box["value"] = text_box["value"][:-1]
                            else:
                                if len(text_box["value"]) < 25:
                                    text_box["value"] += event.unicode
        # Draw every button
        for button in self.buttons:
            # If mouse hovered on button then change it's color
            if button["edges"][0] <= mouse[0] <= button["edges"][1] and \
                    button["edges"][2] <= mouse[1] <= button["edges"][3]:
                pygame.draw.rect(self.display_surface, BUTTON_ACTIVE_COLOR, button["coords"], 50)
                # If button was clicked
                if click[0]:
                    if button["text"] == "Register":
                        # Registration requirements
                        if len(self.text_boxes[0]["value"]) < 4:
                            self.error_message = "Login must be at least 4 symbols long!"
                        elif db_service.get_user(self.text_boxes[0]["value"]):
                            self.error_message = "This login is already occupied!"
                        elif len(self.text_boxes[1]["value"]) < 8:
                            self.error_message = "Password length must be at least 8 symbols long!"
                        elif self.text_boxes[1]["value"] != self.text_boxes[2]["value"]:
                            self.error_message = "Password and password repeat are different!"
                        else:
                            user = User(self.text_boxes[0]["value"], password_encode(self.text_boxes[1]["value"]))
                            db_service.add(user)
                            print("User registered successfully")
                            return Game()
            else:
                pygame.draw.rect(self.display_surface, BUTTON_IDLE_COLOR, button["coords"], 50)
            # Button text putted inside the button
            self.display_surface.blit(button["text-render"], button["text-coords"])
            # Error message print
            error_render = self.error_font.render(self.error_message, True, ERROR_MESSAGE_COLOR)
            self.display_surface.blit(error_render, self.error_message_coords)
        return self
