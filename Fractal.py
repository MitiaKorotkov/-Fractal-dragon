import graph
import math

alf = 45 * math.pi / 180
def Dragon(n, x0, y0, x1, y1,q):
    if n == 0:
        graph.line(x0, y0, x1, y1)
    else:
        alf1 = alf * q
        _x = math.cos(alf1) * ((x1 - x0) * math.cos(alf1) - (y1 - y0) * math.sin(alf1)) + x0
        _y = math.cos(alf1) * ((x1 - x0) * math.sin(alf1) + (y1 - y0) * math.cos(alf1)) + y0
        Dragon(n - 1, x0, y0, _x, _y,1)
        Dragon(n - 1, _x, _y, x1, y1,-1)

# def lol(n,R):
#     if n == 0:
#         print('lol')
#         graph.circle(0,0,R)
#     else:
#         lol(n-1,R)
#         lol(n-1,R+10)
#
# lol(5,10)
Dragon(16, 100, 100, 300, 100,1)
graph.run()