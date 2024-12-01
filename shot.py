import pygame
from circleshape import CircleShape
from constants import *



class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, SHOT_RADIUS, 2)

    # def update(self, dt):
    #     self.position += self.velocity * dt


    def update(self, dt):
        # Update position based on velocity and time delta
        self.position += self.velocity * dt

        # Check if the shot goes out of bounds
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()  # Remove the shot from the game