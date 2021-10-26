import pygame
import math
from pygame import mixer

# Initialize the game
pygame.init()

# Screen
screen = pygame.display.set_mode((1820, 980))

# Background
background = pygame.image.load('background.png')

# Mario
mario = pygame.image.load('mario.png')
marioX = 20
marioY = 728
marioX_change = 0
marioY_change = 0

# Brick
brick = pygame.image.load('brick.png')

#Block
block = pygame.image.load('block.png')
blockX = 300
blockY = 680
def isContactdown(marioX, marioY, blockX, blockY):
    distance = math.sqrt(math.pow(blockX - marioX, 2) + (math.pow(blockY - marioY, 2)))
    if distance < 27:
        return True
    else:
        return False    

def isContactup(mariox, marioY, blockX, blockY):
    distance = math.sqrt(math.pow(blockX - marioX, 2) + (math.pow(blockY - marioY, 2)))
    if distance < 27:
        return True
    else:
        return False    

# Physics
gravity = 0.4

# Game Loop
running = True
while running:

    screen.blit(background, (0, 0))

    num_of_bricks = 91
    x = 0
    for i in range(num_of_bricks):
        x += 20
        screen.blit(brick, (x, 780))

    num_of_blocks = 12
    blockX = 300
    for i in range(num_of_blocks):
        blockX += 20
        blocks = screen.blit(block, (blockX, blockY))
        contactdown = isContactdown(marioX, marioY, blockX, blockY)
        if contactdown:
            marioY_change = 0      
        contactup = isContactup(marioX, marioY, blockX, blockY - 28)
        if contactup:
            marioY_change = 0
            marioY_change -= gravity
    if marioX == 1820:
        marioX = 20
    if marioX == 0:
        marioX = 20        

    screen.blit(mario, (marioX, marioY))

    marioY_change += gravity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                marioY_change = -10
            if event.key == pygame.K_RIGHT:
                marioX_change = 10
            if event.key == pygame.K_LEFT:
                marioX_change = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                marioX_change = 0

    marioX += marioX_change
    if marioY_change + marioY + mario.get_height() <= 780:
        marioY += marioY_change
 
    pygame.display.update()
