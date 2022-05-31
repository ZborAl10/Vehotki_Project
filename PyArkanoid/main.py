# импортируем модуль Pygame (и инициализируем его), а также все необходимые модули с классами
import pygame
import ball
import block
import wall
import paddle
pygame.init()

# устанавливаем размеры окна игры
WIDTH = 800
HEIGHT = 700
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)

# устанавливаем название, которое будет отображено в верхней части окна игры
TITLE = 'PyArkanoid'
pygame.display.set_caption(TITLE)

# устанавливаем частоту кадров
FPS = 60
clock = pygame.time.Clock()

# создаем необходимые объекты
# шар
ball = ball.Ball()
ball_list = [ball]
# платформа
bat = paddle.Paddle(WIDTH / 2 - paddle.PADDLE_WIDTH / 2, HEIGHT - 64)
bat_list = [bat]
# блоки
DISTANCE_BETWEEN_BLOCKS = 0
blocks = [block.Block(DISTANCE_BETWEEN_BLOCKS + 22 + i * (DISTANCE_BETWEEN_BLOCKS + block.BLOCK_WIDTH),
                      DISTANCE_BETWEEN_BLOCKS + j * (DISTANCE_BETWEEN_BLOCKS + block.BLOCK_WIDTH))
          for i in range(10) for j in range(4)]
#blocks = [block.Block(600, 350), block.Block(100, 250), block.Block(600, 200)]
# стены
walls = [wall.HorizontalWall(-10, 0, 0, 0, 0, HEIGHT),
         wall.HorizontalWall(10 + WIDTH, 0, WIDTH, 0, WIDTH, HEIGHT),
         wall.VerticalWall(0, -10, 0, 0, WIDTH, 0)]
# объединяем все объекты, от которых будет отскакивать шар, в один список
entities = blocks + walls + bat_list

# основной цикл игры
run = True
while run:
    for event in pygame.event.get():     # проверяем события
        if event.type == pygame.QUIT:    # если пользовать нажал на крестик,
            run = False                  # выходим из основного цикла игры

    keys = pygame.key.get_pressed()    # создаем список нажатых в данный момент клавиш
    if keys[pygame.K_d]:               # если нажали клавишу D,
        bat.rect.x += 20               # платформа движется вправо
    if keys[pygame.K_a]:               # если же нажали клавишу A,
         bat.rect.x -= 20              # платформа движется влево
    ball.update()
    for element in entities:
        if ball.horizontal_collide(element):
            ball.horizontal_velocity = -ball.horizontal_velocity
            if type(element) == block.Block:
                blocks.remove(element)
                entities.remove(element)
                continue
            elif type(element) == paddle.Paddle:
                ball.horizontal_velocity = ball.horizontal_velocity / abs(ball.horizontal_velocity) * 6
                ball.vertical_velocity = 4
                continue
        if ball.vertical_collide(element):
            ball.vertical_velocity = -ball.vertical_velocity
            if type(element) == block.Block:
                blocks.remove(element)
                entities.remove(element)
                continue
            elif type(element == paddle.Paddle):
                left_of_bat = bat.rect.left
                ball_centerx = ball.rect.centerx
                ball_centerx -= left_of_bat
                paddle_width = paddle.PADDLE_WIDTH
                if any([0 <= ball_centerx <= paddle_width / 5,
                       paddle_width / 5 * 4 <= ball_centerx <= paddle_width]):
                       ball.horizontal_velocity = ball.horizontal_velocity / abs(ball.horizontal_velocity) * 5
                       ball.vertical_velocity = ball.vertical_velocity / abs(ball.vertical_velocity) * 4
                       continue
                elif any([paddle_width / 5 <= ball_centerx <= paddle_width / 5 * 2,
                       paddle_width / 5 * 3 <= ball_centerx <= paddle_width / 5 * 4]):
                       ball.horizontal_velocity = ball.horizontal_velocity / abs(ball.horizontal_velocity) * 3
                       ball.vertical_velocity = ball.vertical_velocity / abs(ball.vertical_velocity) * 4
                       continue
                else:
                    ball.horizontal_velocity = ball.horizontal_velocity / abs(ball.horizontal_velocity) * 1
                    ball.vertical_velocity = ball.vertical_velocity / abs(ball.vertical_velocity) * 6
                    continue

    if bat.rect.left < 0:
        bat.rect.left = 0
    elif bat.rect.right > WIDTH:
        bat.rect.right = WIDTH
    
    screen.fill((24, 21, 17))
    for element in ball_list + bat_list + blocks:
        screen.blit(element.image, element.rect)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit() # когда выходим из основного цикла, игра завершается
