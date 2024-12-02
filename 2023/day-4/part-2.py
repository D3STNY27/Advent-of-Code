import os
from collections import defaultdict
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    total_cards = len(lines)
    card_count = {i+1: 1 for i in range(total_cards)}
    total_sum = 0
    
    for card_number, line in enumerate(lines, start=1):
        cards = line.split(':')[1].strip()
        winning_cards, owned_cards = cards.split('|')

        winning_set = set(winning_cards.strip().split())
        owned_set = set(owned_cards.strip().split())

        match_set = owned_set.intersection(winning_set)

        for i in range(len(match_set)):
            next_card = (card_number + i + 1)
            if next_card > total_cards:
                continue
            card_count[next_card] += card_count[card_number]
        
        total_sum += card_count[card_number]
    
    print(total_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)