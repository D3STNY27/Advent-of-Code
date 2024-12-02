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

DIGIT_DIRECTION_MAP = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    current_node = (START_X, START_Y)
    tiles_ext = 0
    area = 0

    for line in lines:
        _, _, code_raw = line.split()
        code = code_raw[2:-1]

        steps, direction = int(code[:5], 16), DIGIT_DIRECTION_MAP[code[-1]]
        (xn, yn) = DIRECTION_MAP[direction]
        
        (x, y) = current_node
        (xt, yt) = (x + steps * xn, y + steps * yn)
        current_node = (xt, yt)

        if x==xt:
            tiles_ext += abs(yt - y)
        else:
            tiles_ext += abs(xt - x)
        
        area += (yt + y) * (xt - x)
    
    # Pick's Theorem
    tiles_int = ((area // 2) + 1 - (tiles_ext // 2))

    total_tiles = (tiles_int + tiles_ext)
    print(total_tiles)


lines = read_input_file(file_path="input.txt")
solution(lines)