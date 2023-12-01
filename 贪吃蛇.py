import pygame
import random

# 初始化游戏
pygame.init()

# 游戏窗口大小
window_width = 640
window_height = 480

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇游戏")

# 游戏时钟
clock = pygame.time.Clock()

# 定义蛇的初始位置和移动方向
snake_block_size = 20
snake_speed = 15
snake_direction = "right"

# 定义字体
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 50)


def show_score(score):
    score_text = score_font.render("得分：" + str(score), True, white)
    window.blit(score_text, [10, 10])


def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block_size, snake_block_size])


# 游戏主循环
def game_loop():
    game_over = False
    game_close = False

    # 蛇的初始位置
    x1 = window_width / 2
    y1 = window_height / 2

    # 蛇的初始长度
    snake_list = []
    length_of_snake = 1

    # 生成食物的随机位置
    food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(black)
            game_over_text = font_style.render("游戏结束！按Q退出，按C重新开始", True, red)
            window.blit(game_over_text, [window_width / 6, window_height / 3])
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_direction = "left"
                elif event.key == pygame.K_RIGHT:
                    snake_direction = "right"
                elif event.key == pygame.K_UP:
                    snake_direction = "up"
                elif event.key == pygame.K_DOWN:
                    snake_direction = "down"

        # 蛇移动
        if snake_direction == "left":
            x1 -= snake_block_size
        elif snake_direction == "right":
            x1 += snake_block_size
        elif snake_direction == "up":
            y1 -= snake_block_size
        elif snake_direction == "down":
            y1 += snake_block_size

        # 蛇吃到食物
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0
            length_of_snake += 1

        window.fill(black)
        pygame.draw.rect(window, red, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # 蛇长度控制
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # 蛇碰撞检测
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block_size, snake_list)
        show_score(length_of_snake - 1)
        pygame.display.update()

        # 蛇碰到边界
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()


game_loop()