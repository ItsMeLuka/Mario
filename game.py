import pygame
import math
from pygame import mixer

# Initialize the game
pygame.init()

# Screen
screen = pygame.display.set_mode((1820, 980))

# Background
background = pygame.image.load('background.png')

# Brick
brick = pygame.image.load('brick.png') 
x = 0
# Game Loop
running = True
while running:

    screen.blit(background, (0, 0))

    num_of_bricks = 91
    for i in range(num_of_bricks):
        x += 20
        screen.blit(brick, (x, 780))
        pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
