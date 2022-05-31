import pygame

class HorizontalWall():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        (x4, y4) = (x1, y3)
        topleft = (x1, y1)
        wall_width = x2 - x1
        wall_height = y3 - y1
        self.rect = pygame.Rect(topleft, (wall_width, wall_height))

class VerticalWall():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        (x4, y4) = (x3, y1)
        topleft = (x1, y1)
        wall_width = x3 - x2
        wall_height = y2 - y1
        self.rect = pygame.Rect(topleft, (wall_width, wall_height))
