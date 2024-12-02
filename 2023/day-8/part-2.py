import os
from math import gcd

os.system('cls')

    
def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def calculate_steps(src: str, instructions: str, node_map: dict):
    steps, idx = 0, 0
    current_node = src

    while not current_node.endswith('Z'):
        move = instructions[idx % len(instructions)]
        current_node = node_map[current_node][move]
        idx += 1
        steps += 1
    
    return steps


def solution(lines: list[str]):
    instructions = lines[0]
    node_map = {}
    starting_nodes = []

    for line in lines[2:]:
        tokens = [token.strip() for token in line.split('=')]
        src, (dst_l, dst_r) = tokens[0], [token.strip() for token in tokens[1][1:-1].split(',')]
        node_map[src] = {
            'L': dst_l,
            'R': dst_r
        }

        if src[-1]=='A':
            starting_nodes.append(src)

    current_lcm = 1
    for src in starting_nodes:
        steps = calculate_steps(src, instructions, node_map)
        current_lcm = abs(current_lcm * steps) // gcd(current_lcm, steps)
    
    print(current_lcm)


lines = read_input_file(file_path="input.txt")
solution(lines)