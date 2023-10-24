import sys
import turtle as t


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


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    t.title(f'Turtle Graphics Demo using python {get_python_version()}')
    # draw_geometric_pattern()
    draw_star_shape()
