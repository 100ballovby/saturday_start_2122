import pygame as pg
from pygame.draw import rect, circle, polygon
import random as r

W = 800
H = 900
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

# Car
img = pg.image.load('car.png').convert_alpha()
img_rect = img.get_rect()
img_copy = img
img_rect_copy = img_rect

# Tree
tree1 = pg.image.load('tree-3.png').convert_alpha()
tree1_rect = tree1.get_rect()
tree1 = pg.transform.scale(tree1, [W * 0.1, H * 0.2])

tree2 = pg.image.load('tree-3.png').convert_alpha()
tree2_rect = tree2.get_rect()
tree2 = pg.transform.scale(tree2, [W * 0.1, H * 0.2])

tree1_rect.x = 10
tree2_rect.x = W - 90
tree1_rect.y = -200
tree2_rect.y = -500

center = W // 2, H * 0.8  # координаты центра картинки
img_rect.center = center  # центирую картинку на экране игры
img_rect_copy.center = center  # центирую картинку на экране игры

WHITE = (255, 255, 255)
GRASS = (35, 145, 50)
SAND = (255, 245, 181)
GRAY = (61, 61, 61)
RED = (209, 4, 66)
ORANGE = (230, 143, 14)

background = pg.Rect(0, 0, W, H)  # фон
road = pg.Rect(0, 0, W / 2, H)  # дорога
road.center = W // 2, H // 2  # выставляю дорогу посередине
border_left = pg.Rect(road.x - W * 0.12, 0, W * 0.12, H)  # левая обочина
border_right = pg.Rect(road.right, 0, W * 0.12, H)  # правая обочина
paddle1 = pg.Rect(road.x, 0, 100, 20)  # препятствие №1
paddle2 = pg.Rect(road.x, -500, 100, 20)  # препятствие №2
restart_button = pg.Rect(0, 0, W * 0.2, H * 0.1)
restart_button.center = W // 2, H // 2
score_rect = pg.Rect(20, 20, W * 0.15, H * 0.05)
high_score_rect = pg.Rect(20, score_rect.x + H * 0.053, W * 0.215, H * 0.05)


def moving(obj, speed, l_side, r_side):
    obj.x += speed
    if obj.right >= r_side.left:  # если машина коснулась правой обочины
        obj.right = r_side.left - 10
    elif obj.left <= l_side.right:  # если машина коснулась левой обочины
        obj.left = l_side.right + 10


def paddle_moving(obj, surf, s_height, jump):
    global score, high_score

    if obj.y >= s_height:
        x = r.randint(1, 3)
        if x == 1:
            obj.x = surf.x
        elif x == 2:
            obj.center = surf.center
        else:
            obj.right = surf.right
        obj.y = -jump
        score += 1
    if score > high_score:
        high_score = score


def tree_motion(obj, s_height, speed, jump):
    obj.y += speed   # перемещение
    if obj.y >= s_height:  # если объект ушел за нижнюю границу
        obj.y = -jump  # переношу объект за пределы верхней границы


def show_text(text, size, color, x, y, surf):
    pg.font.init()
    font = pg.font.SysFont('comicsans', size)
    msg = font.render(text, True, color)
    surf.blit(msg, [x, y])


car_speed = 0  # начальная скорость машины
angle = 0  # угол поворота картинки изначально
score = 0  # очки за игровую сессию
high_score = 0  # рекорд

finished = False
game_over = False
while not finished:

    while game_over:
        screen.fill(WHITE)
        rect(screen, GRASS, restart_button)

        rect(screen, ORANGE, score_rect)  # поверхность для отображения очков
        rect(screen, ORANGE, high_score_rect)  # поверхность для отображения рекорда
        show_text(f'Score: {score}', 24, WHITE, score_rect.x + 10, score_rect.y, screen)
        show_text(f'High score: {high_score}', 24, WHITE, high_score_rect.x + 10, high_score_rect.y, screen)
        show_text('Restart', 36, WHITE, restart_button.x + 10, restart_button.y + 15, screen)
        show_text('Game Over!', 48, RED, restart_button.x - 30, restart_button.y - 100, screen)
        pg.display.update()


        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = False
                finished = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    paddle1.y = 0
                    paddle2.y = -500
                    game_over = False

    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                car_speed += 10
                angle = -10
            if event.key == pg.K_LEFT:
                car_speed -= 10
                angle = 10
            img_copy = pg.transform.rotate(img, angle)
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                car_speed -= 10
            if event.key == pg.K_LEFT:
                car_speed += 10
            angle = 0
            img_copy = pg.transform.rotate(img, angle)

    screen.fill(WHITE)

    # отрисовываю декорации
    rect(screen, GRASS, background)  # фон игры
    rect(screen, GRAY, road)  # дорога
    rect(screen, SAND, border_left)  # левая обочина
    rect(screen, SAND, border_right)  # правая обочина
    rect(screen, WHITE, [W // 2, 0, 5, H])  # полоса разметки
    rect(screen, RED, paddle1)  # препятствие №1
    rect(screen, RED, paddle2)  # препятствие №2

    screen.blit(img_copy, img_rect_copy)
    screen.blit(tree1, tree1_rect)
    screen.blit(tree2, tree2_rect)

    rect(screen, ORANGE, score_rect)  # поверхность для отображения очков
    rect(screen, ORANGE, high_score_rect)  # поверхность для отображения рекорда
    show_text(f'Score: {score}', 24, WHITE, score_rect.x + 10, score_rect.y, screen)
    show_text(f'High score: {high_score}', 24, WHITE, high_score_rect.x + 10, high_score_rect.y, screen)
    pg.display.update()

    # Логика игры
    moving(img_rect, car_speed, border_left, border_right)
    paddle1.y += 10
    paddle2.y += 10

    paddle_moving(paddle1, road, H, H * 0.2)
    paddle_moving(paddle2, road, H, H * 0.8)

    tree_motion(tree1_rect, H, 10, H * 0.2)
    tree_motion(tree2_rect, H, 10, H)

    if img_rect_copy.colliderect(paddle1) or img_rect_copy.colliderect(paddle2):
        score = 0
        game_over = True
