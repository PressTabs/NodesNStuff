from collections import namedtuple
from random import randint, random
from matplotlib import pyplot as plt, colors

Node = namedtuple("Node", ["x_pos", "y_pos", "size", "color"])
Line = namedtuple("Line", ["node1", "node2", "thickness", "color"])

MIN_X, MAX_X, MIN_Y, MAX_Y = 0, 255, 0, 255
DEFAULT_SIZE = 2
DEFAULT_COLOR = (0, 0, 0)

NEAREST_NEIGHBOR_BIAS = NNB = 2
MAX_NUMBER_OF_CONNECTIONS = MNC = 2

N = 100
nodes = []
lines = []


#   Returns a dot tuple
def gen_dot() -> type(Node):
    x_pos = randint(MIN_X, MAX_X)
    y_pos = randint(MIN_Y, MAX_Y)
    size = DEFAULT_SIZE if DEFAULT_SIZE is not None else 2 ** (3 * random())
    color = DEFAULT_COLOR if DEFAULT_COLOR is not None else [random(), random(), random()]

    node = Node(x_pos, y_pos, size, color)
    return node


def line_gen(node1: type(Node), node2: type(Node)) -> type(Line):
    color = [(node1.color[i] + node2.color[i]) / 2 for i in range(3)]
    thickness = round((node1.size + node2.size) / 2)

    line = Line(node1, node2, thickness, color)
    return line


def gen_lines(node_list) -> list[Line]:
    linez = []

    for i in range(N):
        for j in range(i, min(i+MNC, N)):
            linez.append(line_gen(node_list[i], node_list[randint(0, N-1)]))

    return linez


def draw(node_list, line_list):
    for i in range(len(line_list)):
        line = line_list[i]
        plt.plot([line.node1.x_pos, line.node2.x_pos], [line.node1.y_pos, line.node2.y_pos],
                 lw=line.thickness, color=colors.to_rgb(line.color))

    for i in range(N):
        node = node_list[i]
        plt.plot(node.x_pos, node.y_pos, marker='o', ms=node.size, color=colors.to_rgb(node.color))

    plt.show()


if __name__ == "__main__":
    nodes = [gen_dot() for _ in range(N)]
    lines = gen_lines(nodes)
    draw(nodes, lines)
