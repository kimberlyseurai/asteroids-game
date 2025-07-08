# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


print("Starting Asteroids!")
print("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()   # Update the screen

if __name__ == "__main__":
    main()
