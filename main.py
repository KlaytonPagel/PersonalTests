import pygame
import sys
import math
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.position = pygame.Vector2(self.rect.center)
        self.velocity = pygame.Vector2(0, 0)

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = pygame.Vector2(position)
        self.velocity = velocity

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vector Shooting")

# Create sprites
all_sprites = pygame.sprite.Group()
player = Player()
bullets = pygame.sprite.Group()
all_sprites.add(player)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.velocity = pygame.Vector2(0, 0)

    if keys[K_UP]:
        player.velocity.y = -5
    if keys[K_DOWN]:
        player.velocity.y = 5
    if keys[K_LEFT]:
        player.velocity.x = -5
    if keys[K_RIGHT]:
        player.velocity.x = 5

    if keys[pygame.K_SPACE]:
        # Create a bullet with the player's position and direction
        bullet_velocity = pygame.Vector2(5, 0).rotate(-player.velocity.angle_to(pygame.Vector2(1, 0)))
        bullet = Bullet(player.rect.center, bullet_velocity)
        bullets.add(bullet)
        all_sprites.add(bullet)

    # Update sprites
    all_sprites.update()

    # Check for collisions between bullets and the screen edges
    for bullet in bullets.copy():
        if not pygame.Rect(0, 0, WIDTH, HEIGHT).colliderect(bullet.rect):
            bullet.kill()

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
