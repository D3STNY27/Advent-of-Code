import os
from enum import Enum
from queue import PriorityQueue

os.system('cls')


class Directions(Enum):
    NORTH = (-1, 0)
    WEST = (0, -1)
    SOUTH = (1, 0)
    EAST = (0, 1)
    IDLE = (0, 0)


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    R, C = len(lines), len(lines[0])
    grid = [list(map(int, list(line))) for line in lines]

    cost_so_far = {
        ((0, 0), Directions.IDLE.value, 0): 0
    }

    frontier = PriorityQueue()
    frontier.put((0, ((0, 0), Directions.IDLE.value, 0)))

    min_heat = float('inf')
    while not frontier.empty():
        (xc, yc), direction, steps = frontier.get()[1]
        rev_direction = (-1 * direction[0], -1 * direction[1])

        if (xc, yc)==(R-1, C-1) and steps >= 4:
            min_heat = cost_so_far[((xc, yc), direction, steps)]
            break
    
        for dir in [Directions.NORTH, Directions.EAST, Directions.SOUTH, Directions.WEST]:
            (xn, yn) = dir.value
            (xt, yt) = (xc + xn, yc + yn)

            if (xt < 0) or (xt >= R) or (yt < 0) or (yt >= C):
                continue

            if rev_direction == dir.value:
                continue

            if direction == dir.value and steps >= 10:
                continue

            if direction != dir.value and direction != (Directions.IDLE.value) and steps < 4:
                continue

            heat = grid[xt][yt]
            cost = heat + cost_so_far[((xc, yc), direction, steps)]

            if direction == dir.value:
                new_steps = steps + 1
            else:
                new_steps = 1
            
            next_node = ((xt, yt), dir.value, new_steps)
            if (next_node not in cost_so_far) or (cost < cost_so_far[next_node]):
                cost_so_far[next_node] = cost
                frontier.put((cost_so_far[next_node], next_node))
    
    print(min_heat)


lines = read_input_file(file_path="input.txt")
solution(lines)