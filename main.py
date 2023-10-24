import sys
import turtle as t
from random import random


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def draw_geometric_pattern():
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(steps)
            t.right(30)
    t.mainloop()


def draw_star_shape():
    t.color('red')
    t.fillcolor('yellow')
    t.begin_fill()
    while True:
        t.forward(200)
        t.left(170)
        if abs(t.pos()) < 1:
            break
    t.end_fill()
    t.mainloop()


def draw_randomly():
    t1 = t.Turtle()
    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        t1.right(angle)
        t1.fd(steps)
    t.mainloop()


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    canvasSize = t.screensize()
    print(f'Turtle canvas size (w,h): ({t.window_width()},{t.window_height()})')
    t.title(f'Turtle Graphics Demo using python {get_python_version()}')
    # draw_geometric_pattern()
    # draw_star_shape()
    draw_randomly()
