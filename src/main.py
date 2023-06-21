import sys, pygame

from src.entity.game import Game
from src.pages.app_state import AppState
from src.pages.title import Title
from settings import *


class Window:
    def __init__(self):
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
        Repeats every frame
        if event type == QUIT, then exit game
        :return: None
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.page = Game()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            self.page = self.page.run()
            pygame.display.update()
            self.clock.tick(FPS)


def main():
    """
    This is main method of the project.
    Here the game object is created and ran.
    :return: None
    """
    window = Window()
    window.run()


if __name__ == "__main__":
    main()
