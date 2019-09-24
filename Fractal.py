import graph
import math


def dragon(n, x0, y0, x1, y1, q):
    if n == 0:
        graph.line(x0, y0, x1, y1)
    else:
        alf1 = alf * q
        _x = math.cos(alf1) * ((x1 - x0) * math.cos(alf1) - (y1 - y0) * math.sin(alf1)) + x0
        _y = math.cos(alf1) * ((x1 - x0) * math.sin(alf1) + (y1 - y0) * math.cos(alf1)) + y0
        dragon(n - 1, x0, y0, _x, _y, 1)
        dragon(n - 1, _x, _y, x1, y1, -1)


if __name__ == '__main__':
    alf = 45 * math.pi / 180
    dragon(16, 100, 100, 400, 400, 1)
    graph.run()
