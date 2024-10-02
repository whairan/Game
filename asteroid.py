import pygame
import circleshape

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0,1)

    def draw(self, screen):
        # pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)


    def update(self, dt):

        self.position +=  self.velocity * dt
