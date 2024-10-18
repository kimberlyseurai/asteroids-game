# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():
    
    newPlayer = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_Clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(255, 182, 193))
        newPlayer.draw(screen)
        pygame.display.flip()
        dt = py_Clock.tick(60) / 1000


if __name__ == "__main__":
    main()