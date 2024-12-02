import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    total_points = 0
    
    for line in lines:
        cards = line.split(':')[1].strip()
        winning_cards, owned_cards = cards.split('|')

        winning_set = set(winning_cards.strip().split())
        owned_set = set(owned_cards.strip().split())

        match_set = owned_set.intersection(winning_set)
        if not match_set:
            continue

        total_points += (2**(len(match_set) - 1))
    
    print(total_points)


lines = read_input_file(file_path="input.txt")
solution(lines)