import pygame

PADDLE_WIDTH = 128
PADDLE_HEIGHT = 64

IMAGE_NAME = 'paddle.png'

class Paddle():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y), (PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image = pygame.image.load(IMAGE_NAME)
