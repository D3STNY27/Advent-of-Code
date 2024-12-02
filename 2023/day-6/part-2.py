import os
from math import sqrt, ceil
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    T = int(''.join(lines[0].split()[1:]))
    D = int(''.join(lines[1].split()[1:]))

    a = ceil((T - sqrt(T*T - 4*D)) / 2)
    b = int((T + sqrt(T*T - 4*D)) / 2)

    if a*(T - a) == D:
        a += 1
    
    if b*(T - b) == D:
        b -= 1
    
    num_sols = (b - a + 1)
    print(num_sols)


lines = read_input_file(file_path="input.txt")
solution(lines)