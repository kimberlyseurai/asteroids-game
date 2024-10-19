# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_Clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    
    newPlayer = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
 
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        screen.fill(color=(255, 182, 193))
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        dt = py_Clock.tick(60) / 1000


if __name__ == "__main__":
    main()