import os
from enum import Enum

os.system('cls')


START_X = 0
START_Y = 0

class Directions(Enum):
    NORTH = (0, 1)
    WEST = (-1, 0)
    SOUTH = (0, -1)
    EAST = (1, 0)


DIRECTION_MAP = {
    'R': Directions.EAST.value,
    'D': Directions.SOUTH.value,
    'L': Directions.WEST.value,
    'U': Directions.NORTH.value
}


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    current_node = (START_X, START_Y)
    row_cut_edges = {}
    boundary = set()
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')

    for line in lines:
        tokens = line.split()
        (xn, yn), steps = DIRECTION_MAP[tokens[0]], int(tokens[1])
        
        (x, y) = current_node
        (xt, yt) = (x + steps * xn, y + steps * yn)
        current_node = (xt, yt)

        if (x == xt):
            for i in range(min(y, yt), max(y, yt)+1):
                boundary.add((x, i))

                if i not in row_cut_edges:
                    row_cut_edges[i] = [(x, y, yt)]
                else:
                    row_cut_edges[i].append((x, y, yt))
        else:
            for j in range(min(x, xt), max(x, xt)+1):
                boundary.add((j, y))

        min_x, min_y = min(min_x, xt), min(min_y, yt)
        max_x, max_y = max(max_x, xt), max(max_y, yt)
    
    area_sum = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in boundary:
                area_sum += 1
                continue

            inside = False
            cut_count = 0
            for (x_edge, y1, y2) in sorted(row_cut_edges[y]):
                if x < x_edge:
                    continue

                if y==max(y1, y2):
                    continue

                inside = not inside
                cut_count += 1
            
            if cut_count % 2 != 0:
                area_sum += 1

    print(area_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)