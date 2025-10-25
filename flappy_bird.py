import pygame
import random
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Python")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Variabel Game
gravity = 0.5
bird_movement = 0
game_active = True
score = 0

# Bird
bird = pygame.Rect(50, HEIGHT//2, 30, 30)

# Pipes
pipe_width = 70
pipe_height = random.randint(150, 400)
pipe_gap = 150
pipe_x = WIDTH

font = pygame.font.SysFont(None, 40)

def draw_pipes(x, height):
    # Top pipe
    pygame.draw.rect(screen, GREEN, (x, 0, pipe_width, height))
    # Bottom pipe
    pygame.draw.rect(screen, GREEN, (x, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap))

def display_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -10
            if event.key == pygame.K_SPACE and not game_active:
                # Restart game
                game_active = True
                bird.y = HEIGHT//2
                bird_movement = 0
                pipe_x = WIDTH
                score = 0

    screen.fill(BLUE)

    if game_active:
        # Bird
        bird_movement += gravity
        bird.y += bird_movement
        pygame.draw.rect(screen, RED, bird)

        # Pipes
        pipe_x -= 4
        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            pipe_height = random.randint(150, 400)
            score += 1
        draw_pipes(pipe_x, pipe_height)

        # Collision
        if bird.y <= 0 or bird.y >= HEIGHT:
            game_active = False
        if bird.colliderect(pygame.Rect(pipe_x, 0, pipe_width, pipe_height)) or bird.colliderect(pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_height - pipe_gap)):
            game_active = False

        display_score(score)
    else:
        msg = font.render("Game Over! Press SPACE", True, BLACK)
        screen.blit(msg, (20, HEIGHT//2 - 20))

    pygame.display.update()
    clock.tick(FPS)
