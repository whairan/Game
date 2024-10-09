import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import random
import sys
pygame.init

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player((SCREEN_WIDTH/ 2),( SCREEN_HEIGHT /2))
    AsteroidField()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #color the backgrund
        screen.fill("black")
        for u in updatable:
            u.update(dt)
        # player.update(dt)
            
        for d in drawable:
            d.draw(screen)
        # player.draw(screen)

        for ast in asteroids:
            if ast.collision(player):
                sys.exit("Game Over!")
        
        for ast in asteroids:
            for shot in shots:
                if shot.collision(ast):
                    ast.split()
                    shot.kill()


        
        #refresh the screen
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
