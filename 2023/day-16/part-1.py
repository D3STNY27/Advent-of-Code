import os
from enum import Enum

os.system('cls')

class Directions(Enum):
    NORTH = (-1, 0)
    WEST = (0, -1)
    SOUTH = (1, 0)
    EAST = (0, 1)


MIRROR_MAP = {
    "\\": {
        Directions.EAST: Directions.SOUTH,
        Directions.WEST: Directions.NORTH,
        Directions.NORTH: Directions.WEST,
        Directions.SOUTH: Directions.EAST
    },
    '/': {
        Directions.EAST: Directions.NORTH,
        Directions.WEST: Directions.SOUTH,
        Directions.SOUTH: Directions.WEST,
        Directions.NORTH: Directions.EAST
    }
}


SPLITTER_MAP = {
    '|': {
        Directions.NORTH: [Directions.NORTH],
        Directions.WEST: [Directions.NORTH, Directions.SOUTH],
        Directions.SOUTH: [Directions.SOUTH],
        Directions.EAST: [Directions.NORTH, Directions.SOUTH]
    },
    '-': {
        Directions.NORTH: [Directions.WEST, Directions.EAST],
        Directions.WEST: [Directions.WEST],
        Directions.SOUTH: [Directions.WEST, Directions.EAST],
        Directions.EAST: [Directions.EAST]
    }
}


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    R, C = len(lines), len(lines[0])
    grid = [list(line) for line in lines]

    queue = [(0, 0, Directions.EAST)]
    visited = set((0, 0, Directions.EAST))
    energized = set()

    while queue:
        (x, y, current_direction) = queue[-1]
        tile = grid[x][y]
        queue = queue[:-1]

        energized.add((x, y))
        visited.add((x, y, current_direction))

        if tile=='.':
            target_direction = current_direction
            (xn, yn) = target_direction.value
            (xt, yt) = (x + xn, y + yn)

            if (0 <= xt < R) and (0 <= yt < C) and (xt, yt, target_direction) not in visited:
                queue.append((xt, yt, target_direction))

        elif tile in SPLITTER_MAP.keys():
            if current_direction not in SPLITTER_MAP[tile]:
                continue

            for target_direction in SPLITTER_MAP[tile][current_direction]:
                (xn, yn) = target_direction.value
                (xt, yt) = (x + xn, y + yn)

                if (0 <= xt < R) and (0 <= yt < C) and (xt, yt, target_direction) not in visited:
                    queue.append((xt, yt, target_direction))
        
        else:
            if current_direction not in MIRROR_MAP[tile]:
                continue

            target_direction = MIRROR_MAP[tile][current_direction]
            (xn, yn) = target_direction.value
            (xt, yt) = (x + xn, y + yn)

            if (0 <= xt < R) and (0 <= yt < C) and (xt, yt, target_direction) not in visited:
                queue.append((xt, yt, target_direction))

    print(len(energized))

lines = read_input_file(file_path="input.txt")
solution(lines)