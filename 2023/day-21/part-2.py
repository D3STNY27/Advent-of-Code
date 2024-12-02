import os
from enum import Enum
from pprint import pprint
from time import perf_counter

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    MAX_STEPS = 1000
    grid = [list(line) for line in lines]
    R, C = len(grid), len(grid[0])
    print(R, C)
    
    start_r, start_c = (-1, -1)
    for r, row in enumerate(grid):
        try:
            c = row.index('S')
            start_r, start_c = (r, c)
            break
        except:
            continue
    
    queue, visited = [], set()
    node_count = 0

    if MAX_STEPS % 2 == 0:
        queue.append((start_r, start_c, 0))
        visited.add((start_r, start_c))
    else:
        for (xn, yn) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xt, yt = start_r + xn, start_c + yn

            if xt < 0 or xt >= R or yt < 0 or yt >= C:
                continue

            if grid[xt][yt]=='#':
                continue

            queue.append((xt, yt, 1))
            visited.add((xt, yt))

    print(queue, visited)
    while queue:
        x, y, steps = queue[0]
        queue = queue[1:]

        node_count += 1
        #print(x, y, steps)
        
        if steps >= MAX_STEPS:
            continue

        for (xn, yn) in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
            xt, yt = x + xn, y + yn

            if grid[xt % R][yt % C]=='#':
                continue

            if grid[x % R][yt % C]=='#' and grid[xt % R][y % C]=='#':
                continue

            if (xt, yt) in visited:
                continue

            queue.append((xt, yt, steps + 2))
            visited.add((xt, yt))
        
        for (xn, yn) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xt, yt = x + 2 * xn, y + 2 * yn

            if grid[xt % R][yt % C]=='#':
                continue

            if grid[(x + xn) % R][(y + yn) % C]=='#':
                continue

            if (xt, yt) in visited:
                continue

            queue.append((xt, yt, steps + 2))
            visited.add((xt, yt))
    
    print(node_count)


lines = read_input_file(file_path="sample_input.txt")
solution(lines)