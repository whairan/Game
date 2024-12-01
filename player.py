import pygame
import circleshape
from constants import *
from shot import Shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
        self.timer = 0
        if self.shoot():
            self.timer = PLAYER_SHOOT_COOLDOWN

        if self.timer > 0:
            "do nothing"


    

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.triangle(), 3)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_j]:
            self.rotate(-dt)
        if keys[pygame.K_l]:
            self.rotate(dt)

        if keys[pygame.K_i]:
            self.move(dt)
        if keys[pygame.K_k]:
            self.move(-dt)


        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN
        if self.timer > 0:    
            self.timer -= dt

    
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # def shoot(self): 
    #     shot = Shot(self.position.x, self.position.y)
    #     shot_velocity = pygame.Vector2(0, 1)
    #     shot_velocity.rotate(self.rotation) 
    #     shot_velocity *= PLAYER_SHOOT_SPEED


    def shoot(self): 
        # Create a shot at the player's position
        shot = Shot(self.position.x, self.position.y)
        
        # Calculate the velocity based on the player's rotation
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation)  # -1 because pygame's (0, -1) is "up"
        shot_velocity *= PLAYER_SHOOT_SPEED
        
        # Assign the velocity to the shot
        shot.velocity = shot_velocity


    # def shoot(self): 
    #     # Calculate the forward direction based on the rotation
    #     forward = pygame.Vector2(0, -1).rotate(self.rotation)  # -1 because (0, -1) is "up" in pygame
        
    #     # Calculate the tip of the triangle (shot's starting position)
    #     shot_position = self.position + forward * self.radius
        
    #     # Create the shot at the calculated position
    #     shot = Shot(shot_position.x, shot_position.y)
        
    #     # Calculate the shot's velocity based on the forward direction
    #     shot_velocity = forward * PLAYER_SHOOT_SPEED
        
    #     # Assign the velocity to the shot
    #     shot.velocity = shot_velocity