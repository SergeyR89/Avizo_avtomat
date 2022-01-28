from random import randint


def dot_click(actio, dots):
    x, y = dots.values()
    actio.move_by_offset(randint(x[0], x[1]), randint(y[0], y[1])).click().perform()