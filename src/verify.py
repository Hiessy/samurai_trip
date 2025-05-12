import pygame
import os

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Samurai Animation")

# Load sprite sheet
sprite_sheet = pygame.image.load(os.path.join('..','assets', 'img', 'samurai.png')).convert_alpha()

# Check dimensions
print(f"Sprite sheet size: {sprite_sheet.get_size()}")