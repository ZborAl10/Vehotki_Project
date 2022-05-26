import pygame

BLOCK_WIDTH = 75
BLOCK_HEIGHT = 75

IMAGE_NAME = 'copper.png'

class Block():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y), (BLOCK_WIDTH, BLOCK_HEIGHT))
        self.image = pygame.image.load(IMAGE_NAME)
