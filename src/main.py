import pygame
import sys

from settings import *
from src.entity.game import Game
from src.pages.app_state import AppState
from src.pages.title import Title


class Window:
    """
    A class that represents the game window and handles the main game loop.

    Attributes:
        screen (pygame.Surface): The game window surface.
        clock (pygame.time.Clock): The clock object for controlling the frame rate.
        app_state (AppState): The current state of the application.
        page (Title or Game): The current page or game instance.

    Methods:
        run(): Runs the main game loop.
    """
    def __init__(self):
        """
        Initializes the Window class.
        """
        pygame.init()
        # Screen size
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # Frame timespans
        self.clock = pygame.time.Clock()
        # Window Title
        pygame.display.set_caption(GAME_TITLE)
        # Window Icon
        pygame.display.set_icon(pygame.image.load(GAME_ICON_PATH))
        # Level Creation
        self.app_state = AppState.TITLE_SCREEN
        # Font
        self.page = Title()

    def run(self):
        """
        Runs the main game loop.
        Repeats every frame.
        if event type == QUIT, then exit game
        :return: None
        """
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.page = Game()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            self.page = self.page.run(events)
            pygame.display.update()
            self.clock.tick(FPS)


def main():
    """
    The main method of the project.
    Creates and runs the game window.
    :return: None
    """
    window = Window()
    window.run()


if __name__ == "__main__":
    main()
