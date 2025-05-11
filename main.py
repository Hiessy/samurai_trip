import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Samurai Game")

# Load samurai image (you need to add one to assets/images/)
samurai_img = pygame.image.load("assets/images/samurai.png")
samurai_pos = [100, 300]

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: samurai_pos[0] -= 5
    if keys[pygame.K_RIGHT]: samurai_pos[0] += 5

    screen.fill((50, 50, 50))  # Dark background
    screen.blit(samurai_img, samurai_pos)
    pygame.display.flip()
    clock.tick(60)
