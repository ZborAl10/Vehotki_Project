import pygame
import math

IMAGE_WIDTH = 15
IMAGE_HEIGHT = 15

RECT_WIDTH = int(IMAGE_WIDTH / math.sqrt(2))
RECT_HEIGHT = int(IMAGE_HEIGHT / math.sqrt(2))

x = 400 - 7
y = 700 - 30

IMAGE_NAME = 'ball.png'

class Ball():
    def __init__(self):
        self.rect = pygame.Rect((x, y), (IMAGE_WIDTH, IMAGE_HEIGHT))
        self.image = pygame.image.load(IMAGE_NAME)

        #self.horizontal_velocity = 1
        #self.vertical_velocity = -4

        self.horizontal_velocity = 1
        self.vertical_velocity = -4
        
        self.on_bat = True

        self.health = 3

    def update(self):
        if not self.on_bat:
            self.rect.move_ip(self.horizontal_velocity, self.vertical_velocity)
        
            

        
    def horizontal_collide(self, entity):
        L1 = any([abs(self.rect.left - entity.rect.right) <= abs(self.horizontal_velocity) - 1, abs(self.rect.right - entity.rect.left) <= abs(self.horizontal_velocity) - 1])
        L2 = any([entity.rect.top <= self.rect.bottom <= entity.rect.bottom, entity.rect.top <= self.rect.top <= entity.rect.bottom])
        if all([L1, L2]):
            return True
        else:
            return False
    def vertical_collide(self, entity):
        K1 = any([abs(self.rect.top - entity.rect.bottom) <= abs(self.vertical_velocity) - 1, abs(self.rect.bottom - entity.rect.top) <= abs(self.vertical_velocity) - 1])
        K2 = any([entity.rect.left <= self.rect.right <= entity.rect.right, entity.rect.left <= self.rect.left <= entity.rect.right])
        if all([K1, K2]):
            return True
        else:
            return False
