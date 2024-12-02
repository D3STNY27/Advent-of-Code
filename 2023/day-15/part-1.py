import os

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    hash_sum = 0
    for string in lines[0].split(','):
        current_value = 0
        for c in string:
            current_value += ord(c)
            current_value *= 17
            current_value %= 256
            
        hash_sum += current_value
    print(hash_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)