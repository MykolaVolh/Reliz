import pygame
from pygame.locals import *
import sys
import random

# Initialize pygame
pygame.init()

# Set up the window
back = (200, 255, 255)
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Racing Game")

# Load player images
player1_images = [pygame.transform.scale(pygame.image.load('player1.png'), (50, 50)),
                  pygame.transform.scale(pygame.image.load('player2.png'), (50, 50)),
                  pygame.transform.scale(pygame.image.load('player3.png'), (50, 50)),
                  pygame.transform.scale(pygame.image.load('player4.png'), (50, 50)),
                  pygame.transform.scale(pygame.image.load('player5.png'), (50, 50))]

player2_images = [pygame.transform.scale(pygame.image.load('anotherplayer1.png'), (50, 50)),
                  pygame.transform.scale(pygame.image.load('anotherplayer2.png'), (50, 50)),
                  pygame.transform.scale(pygame.image.load('anotherplayer3.png'), (50, 50)),
                  pygame.transform.scale(pygame.image.load('anotherplayer4.png'), (50, 50)),
                  pygame.transform.scale(pygame.image.load('anotherplayer5.png'), (50, 50))]

# Define the GameSprite class
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = win_width + 20
            self.rect.y = random.randint(50, win_height - 50)

# Define the Player class
class Player(GameSprite):
    def __init__(self, images, *args, **kwargs):
        super().__init__(images[0], *args, **kwargs)
        self.images = images
        self.frame = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        elif keys[K_DOWN]:
            self.rect.y += self.speed

    def animation(self):
        self.frame += 1
        if self.frame >= len(self.images):
            self.frame = 0
        self.image = self.images[self.frame]

# Define the Obstacle class
class Obstacle(GameSprite):
    def __init__(self, x, y, width, height, speed):
        super().__init__(pygame.Surface((width, height)), x, y, width, height, speed)
        self.image.fill((255, 0, 0))  # Red color for the obstacle

# Create player objects
player1 = Player(player1_images, 20, 200, 50, 50, 5)
player2 = Player(player2_images, 20, 300, 50, 50, 5)

# Create obstacle objects
obstacles = pygame.sprite.Group()
for _ in range(5):
    obstacle = Obstacle(random.randint(200, win_width - 100), random.randint(50, win_height - 50), 30, 30, 3)
    obstacles.add(obstacle)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Handle player updates and animations
    player1.update()
    player1.animation()
    player2.update()
    player2.animation()

    # Update obstacles
    obstacles.update()

    # Check for collisions with obstacles
    collisions = pygame.sprite.spritecollideany(player1, obstacles) or pygame.sprite.spritecollideany(player2, obstacles)
    if collisions:
        running = False

    # Clear the screen
    window.fill(back)

    # Draw players and obstacles
    player1.reset()
    player2.reset()
    obstacles.draw(window)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

# Game over
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, (255, 0, 0))
window.blit(game_over_text, (win_width // 2 - 100, win_height // 2))
pygame.display.update()

# Wait for a moment before quitting
pygame.time.delay(2000)

pygame.quit()
sys.exit()
