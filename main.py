import pygame
from config import *
#Great
# there will be main

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        self.running = True

def main():
    game = Game()


if __name__ == "__main__":
    main()