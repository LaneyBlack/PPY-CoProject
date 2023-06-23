import pygame
from src.settings import *
from src.pages.login import Login
from src.pages.register import Register


class Title:
    """
    A class that represents the title screen and handles user interface elements for the title screen.

    Attributes:
        display_surface (pygame.Surface): The surface to display the title screen.
        title (pygame.Surface): The rendered title text.
        title_coords (tuple): The coordinates of the title text on the display surface.
        buttons (list): A list of dictionaries representing the buttons in the title screen.

    Methods:
        run(events): Runs the title screen and handles user input events.
    """
    def __init__(self):
        """
        Initializes the Title class.
        """
        # Get Display Surface
        self.display_surface = pygame.display.get_surface()
        screen_width = self.display_surface.get_width()
        # Load title
        font = pygame.font.Font(FONT_PATH, 150)
        self.title = font.render(GAME_TITLE, True, TITLE_COLOR)
        self.title_coords = (screen_width / 2 - 500, 150)
        # Load buttons
        buttons_width = 800  # px
        buttons_height = 100  # px
        buttons_x = (screen_width / 2) - (buttons_width / 2)
        font = pygame.font.Font(FONT_PATH, 90)
        self.buttons = [
            {"coords": [buttons_x, 450, buttons_width, buttons_height],
             "edges": [buttons_x, buttons_x + buttons_width, 450, 450 + buttons_height],
             "text": "Login",
             "text-render": font.render("Login", False, BUTTON_TEXT_COLOR),
             "text-coords": (buttons_x + buttons_width / 2.8, 450)},
            {"coords": [buttons_x, 600, buttons_width, buttons_height],
             "edges": [buttons_x, buttons_x + buttons_width, 600, 600 + buttons_height],
             "text": "Register",
             "text-render": font.render("Register", False, BUTTON_TEXT_COLOR),
             "text-coords": (buttons_x + buttons_width / 3.4, 600)},
        ]

    def run(self, events):
        """
        Runs the title screen and handles user input events.

        Args:
            events (list): A list of pygame events.

        Returns:
            Login or Register: An instance of the Login or Register class based on user selection, or self otherwise.
        """
        # Get mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.display_surface.fill(BACKGROUND_COLOR)
        self.display_surface.blit(self.title, self.title_coords)
        # self.display_surface.blit(pygame.image.load("img/background.jpg"),(0,0))
        for button in self.buttons:
            if button["edges"][0] <= mouse[0] <= button["edges"][1] and \
                    button["edges"][2] <= mouse[1] <= button["edges"][3]:
                pygame.draw.rect(self.display_surface, BUTTON_ACTIVE_COLOR, button["coords"], 50)
                if click[0]:
                    if button["text"] == "Login":
                        return Login()
                    elif button["text"] == "Register":
                        return Register()
            else:
                pygame.draw.rect(self.display_surface, BUTTON_IDLE_COLOR, button["coords"], 50)
            self.display_surface.blit(button["text-render"], button["text-coords"])
        return self
