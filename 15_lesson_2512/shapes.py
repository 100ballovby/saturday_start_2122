def draw_square(turtle, x, y, color='#000', size=50):
    """
    Drawing square with Python turtle module
    :param turtle: turtle object
    :param x: coordinate x of the square
    :param y: coordinate y of the square
    :param color: shape color (in HEX) default black
    :param size: side size of the square default 50px
    :return: None
    """
    turtle.goto(x, y)  # перейти в х, у
    turtle.down()  # опустить перо
    turtle.color(color)  # определяю цвет черепашки
    for i in range(4):  # повторить 4 раза
        turtle.fd(size)  # вперед на size шагов
        turtle.rt(90)  # повернуть вправо на 90 градусов
    turtle.up()  # поднять перво (перестать рисовать)
    return None


def draw_triangle(turtle, x, y, color='#000', size=50):
    """
    Drawing triangle with Python turtle module
    :param turtle: turtle object
    :param x: coordinate x of the square
    :param y: coordinate y of the square
    :param color: shape color (in HEX) default black
    :param size: side size of the square default 50px
    :return: None
    """
    turtle.goto(x, y)  # перейти в х, у
    turtle.down()  # опустить перо
    turtle.color(color)  # определяю цвет черепашки
    for i in range(3):  # повторить 3 раза
        turtle.fd(size)  # вперед на size шагов
        turtle.lt(120)  # повернуть вправо на 90 градусов
    turtle.up()  # поднять перво (перестать рисовать)
    return None


def draw_star(turtle, x, y, color='#000', size=50):
    """
    Drawing triangle with Python turtle module
    :param turtle: turtle object
    :param x: coordinate x of the square
    :param y: coordinate y of the square
    :param color: shape color (in HEX) default black
    :param size: side size of the square default 50px
    :return: None
    """
    turtle.goto(x, y)  # перейти в х, у
    turtle.down()  # опустить перо
    turtle.color(color)  # определяю цвет черепашки
    for i in range(5):  # повторить 3 раза
        turtle.fd(size)  # вперед на size шагов
        turtle.rt(144)  # повернуть вправо на 90 градусов
    turtle.up()  # поднять перво (перестать рисовать)
    return None


def x_angle(turtle, x, y, corners, color='#000', size=50):
    """
    Draws any regular polygon along a given number of corners
    :param turtle: turtle object
    :param x: coordinate x of the square
    :param y: coordinate y of the square
    :param corners: count of angles
    :param color: shape color (in HEX) default black
    :param size: side size of the square default 50px
    :return: None
    """
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    for i in range(corners):
        turtle.fd(size)
        turtle.lt(360 / corners)
    turtle.up()



