import pygame
import ball
import block
pygame.init()


WIDTH = 800
HEIGHT = 700
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)

TITLE = 'PyArkanoid'
pygame.display.set_caption(TITLE)

FPS = 60
clock = pygame.time.Clock()

paddle_image = pygame.image.load('paddle.png')
PADDLE_WIDTH = 128
PADDLE_HEIGHT = 64
PADDLE_SIZE = (PADDLE_WIDTH, PADDLE_HEIGHT)
paddle = pygame.Rect((WIDTH / 2 - PADDLE_WIDTH / 2, HEIGHT - 64), PADDLE_SIZE)

block_image = pygame.image.load('copper.png')
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50
BLOCK_SIZE = (BLOCK_WIDTH, BLOCK_HEIGHT)
#block = pygame.Rect((10, 10), BLOCK_SIZE)

ball = ball.Ball()

DISTANCE_BETWEEN_BLOCKS = 13
blocks = [block.Block(DISTANCE_BETWEEN_BLOCKS + i * (DISTANCE_BETWEEN_BLOCKS + block.BLOCK_WIDTH), DISTANCE_BETWEEN_BLOCKS + j * (DISTANCE_BETWEEN_BLOCKS + block.BLOCK_WIDTH))
          for i in range(9) for j in range(4)]
entities = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        paddle = paddle.move(10, 0)
    if keys[pygame.K_a]:
        paddle = paddle.move(-10, 0)

    for element in blocks:
        if ball.horizontal_collide(element):
            ball.horizontal_velocity *= -1
            if type(element) == block.Block:
                entities.remove(element)

    screen.fill((0, 0, 0))
    for element in blocks:
        screen.blit(element.image, element.rect)
    screen.blit(ball.image, ball.outter_rect)
    ball.update()
    
    #screen.blit(paddle_image, paddle)
    #screen.blit(block_image, block)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
