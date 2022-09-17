from collections import namedtuple
from random import randint, random

Node = namedtuple("Node", ["x_pos", "y_pos", "size", "color"])
Line = namedtuple("Line", ["node1", "node2", "thickness", "color"])

MIN_X, MAX_X, MIN_Y, MAX_Y = 0, 255, 0, 255
DEFAULT_SIZE = 4
DEFAULT_COLOR = None

NEAREST_NEIGHBOR_BIAS = NNB = 2

N = 100
nodes = []
lines = []


#   Returns a dot tuple
def gen_dot() -> type(Node):
    x_pos = randint(MIN_X, MAX_X)
    y_pos = randint(MIN_Y, MAX_Y)
    size = DEFAULT_SIZE if DEFAULT_SIZE is not None else 2 ** (3 * random())
    color = DEFAULT_COLOR if DEFAULT_COLOR is not None else [randint(0, 255), randint(0, 255), randint(0, 255)]

    node = Node(x_pos, y_pos, size, color)
    return node


def line_gen(node1: type(Node), node2: type(Node)) -> type(Line):
    color = [round((node1.color[i] + node2.color[i]) / 2) for i in range(3)]
    thickness = round((node1.size + node2.size) / 2)

    line = Line(node1, node2, thickness, color)
    return line


if __name__ == "__main__":
    nodes = [gen_dot() for _ in range(N)]
    lines = [line_gen(nodes[i], nodes[j]) for i in range(N) for j in range(i, N)]
    print(nodes)
    print(lines)
