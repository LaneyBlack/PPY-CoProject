import sys, pygame
from settings import *
from debug import debug


class Game:
    def __init__(self):
        pygame.init()
        # Initialise Screen size
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # Frame timespans
        self.clock = pygame.time.Clock()
        # Window Title
        pygame.display.set_caption(GAME_TITLE)
        # Window Icon
        pygame.display.set_icon(pygame.image.load(GAME_ICON_PATH))


    def run(self):
        """
        Repeats every frame
        if event type == QUIT, then exit game
        :return: None
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill("black")
            debug("Hello World")
            pygame.display.update()
            self.clock.tick(FPS)



def main():
    """
    This is main method of the project.
    Here the game object is created and runned.
    :return:
    """
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
