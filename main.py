
import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
       
        updatable.update(dt)
        screen.fill("pink")  # Fill screen with black

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()   # Update the screen
        
        dt = clock.tick(60) / 1000
        
        
        

if __name__ == "__main__":
    main()
