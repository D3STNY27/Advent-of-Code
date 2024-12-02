import os
from enum import Enum
from random import choice

os.system('cls')


class Directions(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)


BEND_MAP = {
    'L': {
        Directions.LEFT: Directions.UP,
        Directions.DOWN: Directions.RIGHT
    },
    'J': {
        Directions.RIGHT: Directions.UP,
        Directions.DOWN: Directions.LEFT
    },
    '7': {
        Directions.UP: Directions.LEFT,
        Directions.RIGHT: Directions.DOWN
    },
    'F': {
        Directions.UP: Directions.RIGHT,
        Directions.LEFT: Directions.DOWN
    },
    '|': {
        Directions.DOWN: Directions.DOWN,
        Directions.UP: Directions.UP
    },
    '-': {
        Directions.LEFT: Directions.LEFT,
        Directions.RIGHT: Directions.RIGHT
    }
}

    
def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    grid = [list(line) for line in lines]
    r, c = len(grid), len(grid[0])
    
    s_pos = (-1, -1)
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='S':
                s_pos = (i, j)
    
    loops = []
    for pipe_type in BEND_MAP.keys():
        (x, y) = s_pos
        grid[x][y] = pipe_type
        current_direction = choice(list(BEND_MAP[pipe_type].values()))
        temp_loop = [(x, y, grid[x][y])]

        x_n, y_n = current_direction.value
        x, y = x + x_n, y + y_n
        
        while True:
            if grid[x][y]=='.':
                break

            if current_direction not in BEND_MAP[grid[x][y]]:
                break

            temp_loop.append((x, y, grid[x][y]))
            current_direction = BEND_MAP[grid[x][y]][current_direction]
            x_n, y_n = current_direction.value
            x, y = x + x_n, y + y_n
        
            if x==s_pos[0] and y==s_pos[1] and current_direction in BEND_MAP[grid[x][y]]:
                loops.append(temp_loop)
                break
    
    main_loop = loops[0]
    start_node = (*main_loop[0], 0)
    queue = [start_node]
    visited = set()
    max_steps = float('-inf')

    while queue:
        (x, y, tile, step) = queue[0]
        queue = queue[1:]
        visited.add((x, y))
        if step > max_steps:
            max_steps = step

        for _, next_dir in BEND_MAP[tile].items():
            x_n, y_n = next_dir.value
            if (x + x_n, y + y_n) not in visited:
                queue.append((x + x_n, y + y_n, grid[x + x_n][y + y_n], step+1))
    
    print(max_steps)


lines = read_input_file(file_path="input.txt")
solution(lines)