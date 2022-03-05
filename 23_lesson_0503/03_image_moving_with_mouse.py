import pygame as pg
from pygame.draw import rect, circle, polygon

red = (255, 0, 0)
gray = (150, 150, 150)

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

img = pg.image.load('angry-birds.png')
img_rect = img.get_rect()
img_rect.center = W // 2, H // 2
moving = False

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:  # если кто-то нажал кнопку на мыши
            if img_rect.collidepoint(event.pos):  # если координаты мыши совпадают с квадратом картинки
                moving = True  # разрешаю двигаться

        elif event.type == pg.MOUSEBUTTONUP:  # если отпустили кнопку мыши
            moving = False  # запрещаю двигаться

        elif event.type == pg.MOUSEMOTION and moving:  # если мышь двигается и moving = True
            img_rect.move_ip(event.rel)  # event.rel - в постоянном режиме считывает положение мыши и пишет координаты
            # move_ip - сдвигает объект по координатам, которые передаются в скобках

    screen.fill(gray)
    screen.blit(img, img_rect)
    rect(screen, red, img_rect, 2)
    pg.display.update()