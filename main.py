import math
from collections import namedtuple
from random import randint, random
from matplotlib import pyplot as plt, colors

Node = namedtuple("Node", ["x_pos", "y_pos", "size", "color"])
Line = namedtuple("Line", ["node1", "node2", "thickness", "color"])

MIN_X, MAX_X, MIN_Y, MAX_Y = 0, 255, 0, 255
DEFAULT_SIZE = 4
DEFAULT_COLOR = None
DEFAULT_THICKNESS = 2
SEARCH_RADIUS = 48

NEAREST_NEIGHBOR_BIAS = NNB = 3
MAX_NUMBER_OF_CONNECTIONS = MNC = 3

N = 50
nodes = []
lines = []

plt.figure(figsize=((MAX_X - MIN_X) / 51, (MAX_Y - MIN_Y) / 51))


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
    thickness = DEFAULT_THICKNESS if DEFAULT_THICKNESS is not None else round((node1.size + node2.size) / 2)

    line = Line(node1, node2, thickness, color)
    return line


def weighted_probability(probs) -> int:
    rand = random()
    total = 0
    for i in range(len(probs)):
        total += probs[i]
        if total > rand:
            return i

    return len(probs) - 1


def gen_lines(node_list) -> list[Line]:
    linez = []

    for i in range(N):

        probability_lines = []
        node1 = node_list[i]
        for k in range(min(i + 1, N), N):
            node2 = node_list[k]
            probability_lines.append(1 / (math.dist([node1.x_pos, node1.y_pos], [node2.x_pos, node2.y_pos]) ** NNB))

        summed_probs = sum(probability_lines)
        normalized_probs = [p / summed_probs for p in probability_lines]

        for j in range(min(i + 1, N), min(i + MNC, N)):
            linez.append(line_gen(node1, node_list[min(weighted_probability(normalized_probs) + i + 1, N)]))

    return linez


def gen_lines2(node_list) -> list[Line]:
    linez = []

    for i in range(N):
        node1 = node_list[i]
        for j in range(min(i + 1, N), N):
            node2 = node_list[j]
            dist = math.dist([node1.x_pos, node1.y_pos], [node2.x_pos, node2.y_pos])
            if dist < SEARCH_RADIUS:
                linez.append(line_gen(node1, node2))

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
    lines = gen_lines2(nodes)
    draw(nodes, lines)
