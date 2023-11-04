import sys
import turtle as t
from random import random
from time import perf_counter as clock

from designer import Designer


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


def run_demo_byte_design() -> str:
    t1 = Designer()
    t1.speed(1)
    t1.hideturtle()
    t1.getscreen().delay(4096)
    t1.getscreen().tracer(1024)
    at = clock()
    t1.design(t1.position(), 2)
    et = clock()
    t.mainloop()    
    return f'runtime: {(et-at):.2f} sec.'


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    canvasSize = t.screensize()
    print(f'Turtle canvas size (w,h): ({t.window_width()},{t.window_height()})')
    t.title(f'Turtle Graphics Demo using python {get_python_version()}')
    # draw_geometric_pattern()
    draw_star_shape()
    # draw_randomly()
    # print(f'ByteDesign demo {run_demo_byte_design()}')
