import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randint

W = 1280
H = 720
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Game Variables
speed = 15  # отвечает за скорость передвижения платформы и шарика
pl_x = W // 2
pl_y = H - 100

rad = 40
cir_x = randint(0 + rad, W - rad)
cir_y = 0 - rad

score = 3


def show_text(text, x, y):
    pg.font.init()
    font = pg.font.SysFont('comicsans', 32)  # настройки шрифта
    msg = font.render(text, True, BLACK)
    screen.blit(msg, [x, y])

finished = False
game_over = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill(WHITE)
    platform = rect(screen, BLACK, [pl_x, pl_y, 200, 50])
    ball = circle(screen, RED, [cir_x, cir_y], rad)

    show_text(f'Score: {score}', 0, 0)
    pg.display.update()

    # Platform moving
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        pl_x -= speed
    if keys[pg.K_RIGHT]:
        pl_x += speed

    # Walls collision
    if platform.right >= W:
        pl_x = W - 205
    if platform.left <= 0:
        pl_x = 5

    # Ball moving
    cir_y += speed
    if cir_y >= H:
        cir_y = 0 - rad
        cir_x = randint(0 + rad, W - rad)
        score -= 1
    if platform.colliderect(ball):
        cir_y = 0 - rad
        cir_x = randint(0 + rad, W - rad)
        score += 1
