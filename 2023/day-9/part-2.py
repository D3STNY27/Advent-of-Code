import os
os.system('cls')

    
def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def find_exterpolation(sequence: list):
    seq_set = set(sequence)

    if len(seq_set)==1:
        return seq_set.pop()
    
    seq_diff = [sequence[i+1] - sequence[i] for i in range(0, len(sequence)-1)]
    return sequence[0] - find_exterpolation(seq_diff)


def solution(lines: list[str]):
    sum_exterpolate = 0
    for sequence in [list(map(int, line.split())) for line in lines]:
        sum_exterpolate += find_exterpolation(sequence)
    print(sum_exterpolate)


lines = read_input_file(file_path="input.txt")
solution(lines)