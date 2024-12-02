import os
from enum import Enum
import numpy as np
from functools import cache
from pprint import pprint

os.system('cls')


class Directions(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3


PREV_ROCKS = {}


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


@cache
def perform_spin(round_rocks: tuple, dir: Directions, shape: tuple):
    R, C = shape
    round_rocks_set = set(round_rocks)
    round_rocks_update = set()
    total_load = 0

    for (r, c) in round_rocks:
        global PREV_ROCKS
        prev_rock = PREV_ROCKS[dir][r][c]
        round_rocks_between = 0
        
        if dir==Directions.NORTH:
            for i in range(prev_rock+1, r):
                if (i, c) in round_rocks_set:
                    round_rocks_between += 1

            pos = (round_rocks_between, c) if prev_rock==-1 else (prev_rock + 1 + round_rocks_between, c)
            round_rocks_update.add(pos)
        elif dir==Directions.WEST:
            for i in range(prev_rock+1, c):
                if (r, i) in round_rocks_set:
                    round_rocks_between += 1

            pos = (r, round_rocks_between) if prev_rock==-1 else (r, prev_rock + 1 + round_rocks_between)
            round_rocks_update.add(pos)
        elif dir==Directions.SOUTH:
            for i in range(r+1, R if prev_rock==-1 else prev_rock):
                if (i, c) in round_rocks_set:
                    round_rocks_between += 1
            
            pos = ((R-1) - round_rocks_between, c) if prev_rock==-1 else (prev_rock - 1 - round_rocks_between, c)
            round_rocks_update.add(pos)
        else:
            for i in range(c+1, C if prev_rock==-1 else prev_rock):
                if (r, i) in round_rocks_set:
                    round_rocks_between += 1
                    
            pos = (r, (C-1) - round_rocks_between) if prev_rock==-1 else (r, prev_rock - 1 - round_rocks_between)
            round_rocks_update.add(pos)
        
        total_load += (R - pos[0])
    
    return tuple(round_rocks_update), total_load


@cache
def perform_spin_cycle(position: tuple, shape: tuple):
    R, C = shape
    next_pos, _ = perform_spin(position, Directions.NORTH, (R, C))
    next_pos, _ = perform_spin(next_pos, Directions.WEST, (R, C))
    next_pos, _ = perform_spin(next_pos, Directions.SOUTH, (R, C))
    next_pos, load = perform_spin(next_pos, Directions.EAST, (R, C))
    return next_pos, load


def solution(lines: list[str]):
    R, C = len(lines), len(lines[0])
    MAX_CYCLES, CALCULATE_CYCLE = 100000, 1000000000
    THRESHOLD_CYCLE = int(MAX_CYCLES / 10)
    
    prev_rock_north = [[-1 for _ in range(C)] for _ in range(R)]
    prev_rock_south = [[-1 for _ in range(C)] for _ in range(R)]
    prev_rock_east = [[-1 for _ in range(C)] for _ in range(R)]
    prev_rock_west = [[-1 for _ in range(C)] for _ in range(R)]

    round_rocks_set = set()
    fix_rocks_set = set()
    
    for i in range(R):
        for j in range(C):
            if lines[i][j]=='#':
                prev_rock_north[i][j] = i 
                fix_rocks_set.add((i, j))
            else:
                prev_rock_north[i][j] = prev_rock_north[i-1][j] if i > 0 else -1
            
            if lines[i][j]=='O':
                round_rocks_set.add((i, j))
    
    for j in range(C):
        for i in range(R):
            if lines[i][j]=='#':
                prev_rock_west[i][j] = j 
            else:
                prev_rock_west[i][j] = prev_rock_west[i][j-1] if j > 0 else -1
    
    for i in range(R-1, -1, -1):
        for j in range(C):
            if lines[i][j]=='#':
                prev_rock_south[i][j] = i 
            else:
                prev_rock_south[i][j] = prev_rock_south[i+1][j] if i < R-1 else -1
    

    for j in range(C-1, -1, -1):
        for i in range(R):
            if lines[i][j]=='#':
                prev_rock_east[i][j] = j 
            else:
                prev_rock_east[i][j] = prev_rock_east[i][j+1] if j < C-1 else -1
        
    global PREV_ROCKS
    PREV_ROCKS = {
        Directions.NORTH: prev_rock_north,
        Directions.WEST: prev_rock_west,
        Directions.SOUTH: prev_rock_south,
        Directions.EAST: prev_rock_east
    }

    sequence, repeat = [], -1
    next_pos = tuple(round_rocks_set)
    for cycle in range(MAX_CYCLES):
        next_pos, load = perform_spin_cycle(next_pos, (R, C))
        print(f'Cycle-{cycle}: {load}')
        if cycle < THRESHOLD_CYCLE:
            continue

        sequence.append(load)
    
    sequence_arr = np.array(sequence)
    for l in range(1, len(sequence_arr)):
        split_arr = np.split(sequence_arr, [i for i in range(l, len(sequence_arr), l)])
        if len(split_arr[-1]) != l:
            split_arr = split_arr[:-1]

        equal_check = True
        for i in range(len(split_arr)-1):
            if not np.array_equal(split_arr[i], split_arr[i+1]):
                equal_check = False
                break
        
        if equal_check:
            repeat = l
            break

    print(sequence_arr[:repeat])
    cycle_offset = (CALCULATE_CYCLE - (repeat * ((CALCULATE_CYCLE - THRESHOLD_CYCLE) // repeat))) - THRESHOLD_CYCLE
    print(sequence_arr[cycle_offset-1])


lines = read_input_file(file_path="input.txt")
solution(lines)