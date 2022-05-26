import pygame
import math

IMAGE_WIDTH = 15
IMAGE_HEIGHT = 15

RECT_WIDTH = int(IMAGE_WIDTH / math.sqrt(2))
RECT_HEIGHT = int(IMAGE_HEIGHT / math.sqrt(2))

x = 400
y = 400

IMAGE_NAME = 'ball.png'

class Ball():
    def __init__(self):
        self.outter_rect = pygame.Rect((x, y), (IMAGE_WIDTH, IMAGE_HEIGHT))
        self.rect = pygame.Rect((x, y), (RECT_WIDTH, RECT_HEIGHT))
        
        self.image = pygame.image.load(IMAGE_NAME)

        self.horizontal_velocity = 1
        self.vertical_velocity = -1
        self.velocity = (self.horizontal_velocity, self.vertical_velocity)

    def update(self):
        self.rect.move_ip(*self.velocity)
        self.outter_rect.move_ip(*self.velocity)
        
    def horizontal_collide(self, entity):
        if abs(self.rect.left - entity.rect.right) <= 2 or abs(self.rect.right - entity.rect.left) <= 2:
            return True
        else:
            return False
    def vertical_collide(self, entity):
        if abs(self.rect.bottom - entity.top) <= 2 or abs(self.rect.top - self.entity.bottom) <= 2:
            return True
        else:
            return False
