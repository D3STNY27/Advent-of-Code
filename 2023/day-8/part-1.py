import os
os.system('cls')

    
def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    instructions = lines[0]
    node_map = {}

    for line in lines[2:]:
        tokens = [token.strip() for token in line.split('=')]
        src, (dst_l, dst_r) = tokens[0], [token.strip() for token in tokens[1][1:-1].split(',')]
        node_map[src] = {
            'L': dst_l,
            'R': dst_r
        }
    
    steps, idx = 0, 0
    current_src = 'AAA'

    while current_src != 'ZZZ':
        move = instructions[idx % len(instructions)]
        current_src = node_map[current_src][move]
        idx += 1
        steps += 1
    
    print(steps)


lines = read_input_file(file_path="input.txt")
solution(lines)