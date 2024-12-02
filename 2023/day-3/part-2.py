import os
import re
os.system('cls')


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_part_list_from_line(line: str):
    regex_iter = re.finditer('[0-9]+', line)

    part_list = []
    for iter in regex_iter:
        part_number, (start_idx, end_idx) = iter.group(), iter.span()
        part_list.append((int(part_number), start_idx, end_idx-1))
    return part_list


def get_gears_list_from_line(line: str, line_num: int):
    symbols_list = []
    for i, char in enumerate(line):
        if char == '*':
            symbols_list.append((line_num, i))
    return symbols_list


def get_valid_parts(symbol: tuple, line_part_map: dict):
    points = [(symbol[0] + x, symbol[1] + y) for (x, y) in DIRECTIONS]
    valid_part_set = set()

    for (x, y) in points:
        if x not in line_part_map:
            continue
    
        y_ranges = line_part_map[x]
        for (y_start, y_end) in y_ranges:
            if y_start <= y <= y_end:
                valid_part_set.add((x, y_start, y_end))
    
    if len(valid_part_set)!=2:
        return set()
    
    return valid_part_set


def solution(lines: list[str]):
    gears = []
    part_id_pos_map = {}
    line_part_map = {}

    for line_number, line in enumerate(lines):
        part_list = get_part_list_from_line(line)
        part_id_pos_map.update({(line_number, start_x, end_x): part_id for part_id, start_x, end_x in part_list})
        line_part_map[line_number] = [(start_x, end_x) for _, start_x, end_x in part_list]

        gears_list = get_gears_list_from_line(line, line_number)
        gears.extend(gears_list)
    
    # print(symbols)
    # print(part_id_pos_map)
    # print(line_part_map)
    
    total_sum = 0
    unique_part_set = set()
    for gear in gears:
        valid_parts = get_valid_parts(gear, line_part_map)
        if valid_parts:
            part_1, part_2 = valid_parts
            gear_ratio = part_id_pos_map[part_1] * part_id_pos_map[part_2]
            total_sum += gear_ratio

    print(total_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)