import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 





def main():
    print("Starting Asteroids!")



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()



if __name__ == "__mian__":
    main()


