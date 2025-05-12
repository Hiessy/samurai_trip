import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Samurai Animation")

# Load sprite sheet
try:
    sprite_sheet = pygame.image.load(os.path.join('assets', 'img', 'samurai.png')).convert_alpha()
except Exception as e:
    print(f"Error loading sprite sheet: {e}")
    sys.exit()

# Sprite sheet dimensions (1024x1536)
SPRITE_SHEET_WIDTH = 1024
SPRITE_SHEET_HEIGHT = 1536

# Animation settings (adjust based on your sheet layout)
COLUMNS = 4  # Frames per row
ROWS = 6  # Number of rows
FRAME_WIDTH = SPRITE_SHEET_WIDTH // COLUMNS
FRAME_HEIGHT = SPRITE_SHEET_HEIGHT // ROWS

# Extract frames
frames = []
for row in range(ROWS):
    for col in range(COLUMNS):
        frame_rect = pygame.Rect(
            col * FRAME_WIDTH,
            row * FRAME_HEIGHT,
            FRAME_WIDTH,
            FRAME_HEIGHT
        )
        frame = sprite_sheet.subsurface(frame_rect)
        frames.append(frame)

# Animation control
current_frame = 0
animation_speed = 0.1  # Seconds per frame (adjust for speed)
last_update = pygame.time.get_ticks()

# Character position
char_x = SCREEN_WIDTH // 2 - FRAME_WIDTH // 2
char_y = SCREEN_HEIGHT // 2 - FRAME_HEIGHT // 2

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle animation frame updates
    now = pygame.time.get_ticks()
    if now - last_update > animation_speed * 1000:
        current_frame = (current_frame + 1) % len(frames)
        last_update = now

    # Clear screen
    screen.fill((50, 50, 50))  # Dark gray background

    # Draw current frame
    screen.blit(frames[current_frame], (char_x, char_y))

    # Display frame info (debug)
    font = pygame.font.SysFont(None, 24)
    debug_text = f"Frame: {current_frame + 1}/{len(frames)} | Size: {FRAME_WIDTH}x{FRAME_HEIGHT}"
    text_surface = font.render(debug_text, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()