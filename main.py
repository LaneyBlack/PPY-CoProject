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

    def run(self):
        """
        Repeats every frame
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
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
