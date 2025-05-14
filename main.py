import pygame
import sys

# --- Settings ---
SPRITE_SHEET = "assets/img/samurai.png"
ORIG_FRAME_WIDTH = 256
ORIG_FRAME_HEIGHT = 256
COLUMNS = 4
RUNNING_ROW = 1  # 2nd row (0-indexed)
FPS = 8
SPEED = 5
SCALE = 0.5  # Resize to 50%

# --- Init ---
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Samurai Running Fixed + Scaled")
clock = pygame.time.Clock()

# --- Load and scale frames ---
sheet = pygame.image.load(SPRITE_SHEET).convert_alpha()

# Extract specific row
frames = []
for col in range(COLUMNS):
    x = col * ORIG_FRAME_WIDTH
    y = RUNNING_ROW * ORIG_FRAME_HEIGHT
    frame = sheet.subsurface(pygame.Rect(x, y, ORIG_FRAME_WIDTH, ORIG_FRAME_HEIGHT))

    # Resize frame
    new_size = (int(ORIG_FRAME_WIDTH * SCALE), int(ORIG_FRAME_HEIGHT * SCALE))
    frame = pygame.transform.scale(frame, new_size)

    frames.append(frame)

# --- Sprite state ---
x_pos = 70
y_pos = 600 - frames[0].get_height()  # Ground alignment
frame_index = 0
facing_right = True

# --- Game loop ---
running = True
while running:
    keys = pygame.key.get_pressed()
    move = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    if keys[pygame.K_LEFT]:
        move = -SPEED
        facing_right = False
    elif keys[pygame.K_RIGHT]:
        move = SPEED
        facing_right = True

    x_pos += move

    # Draw
    screen.fill((30, 30, 30))

    current_frame = frames[frame_index]
    if not facing_right:
        current_frame = pygame.transform.flip(current_frame, True, False)

    screen.blit(current_frame, (x_pos, y_pos))
    pygame.display.flip()

    if move != 0:
        frame_index = (frame_index + 1) % len(frames)

    clock.tick(FPS)

pygame.quit()
sys.exit()
