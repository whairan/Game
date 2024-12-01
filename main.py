import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import random
import sys
import clock


pygame.init
















import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers for game objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Initialize Player and Asteroid Field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # Game state variables
    score = 0
    high_score = 0  # Add this variable
    game_over = False
    mouse_clicked = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_over:
            # Update high score
            high_score = max(high_score, score)

            # Show home page
            screen.fill("black")
            restart_button_rect = draw_home_page(screen, score, high_score)
            pygame.display.flip()

            # Handle mouse click for restart
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                if not mouse_clicked:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_button_rect.collidepoint(mouse_pos):
                        # Reset all game state
                        updatable.empty()
                        drawable.empty()
                        asteroids.empty()
                        shots.empty()
                        
                        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        AsteroidField()
                        score = 0
                        game_over = False
                        mouse_clicked = True
            else:
                mouse_clicked = False  # Reset mouse click state
        else:
            # Game logic
            screen.fill("black")
            for u in updatable:
                u.update(dt)

            for d in drawable:
                d.draw(screen)

            # Collision checks
            for ast in asteroids:
                if ast.collision(player):
                    game_over = True  # Set game over state
                for shot in shots:
                    if shot.collision(ast):
                        ast.split()
                        shot.kill()
                        score += 1

            pygame.display.flip()
            dt = clock.tick(60) / 1000


def draw_home_page(screen, score, high_score):
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, (255, 255, 255))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))

    # Restart button
    button_font = pygame.font.Font(None, 50)
    button_text = button_font.render("Restart", True, (255, 255, 255))
    restart_button_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

    # Draw UI
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 200))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    pygame.draw.rect(screen, (255, 255, 255), restart_button_rect.inflate(20, 10), 2)
    screen.blit(button_text, restart_button_rect)

    return restart_button_rect

if __name__ == "__main__":
    main()