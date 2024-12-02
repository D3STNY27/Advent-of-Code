import os
from enum import Enum
from functools import cmp_to_key

os.system('cls')

class CardTypes(Enum):
    FIVE_KIND = 7
    FOUR_KIND = 6
    FULL_HOUSE = 5
    THREE_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


CARD_VALUE = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


class Hand:
    def __init__(self, hand: str, bid: str):
        self.hand_str = hand
        self.bid = int(bid)
        self.counts = self.calculate_counts(hand)
        self.type = self.calculate_type()
    

    def calculate_counts(self, hand: str):
        count_map = {}
        for card in hand:
            try:
                count_map[card] += 1
            except:
                count_map[card] = 1
        return count_map


    def calculate_type(self):
        if len(self.counts)==1:
            return CardTypes.FIVE_KIND
        
        if len(self.counts)==2:
            if max(self.counts.values())==4:
                return CardTypes.FOUR_KIND
            else:
                return CardTypes.FULL_HOUSE
    
        if len(self.counts)==3:
            if max(self.counts.values())==3:
                return CardTypes.THREE_KIND
            elif max(self.counts.values())==2:
                return CardTypes.TWO_PAIR
            else:
                return CardTypes.ONE_PAIR
        
        if len(self.counts)==4 and max(self.counts.values())==2:
            return CardTypes.ONE_PAIR
        
        return CardTypes.HIGH_CARD


    def __repr__(self):
        return f'{self.hand_str} {self.type}'


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def compare_hands(hand_a: Hand, hand_b: Hand):
    hand_a_type = hand_a.type.value
    hand_b_type = hand_b.type.value
    
    if hand_a_type != hand_b_type:
        return hand_b_type - hand_a_type
    
    for i in range(5):
        card_a, card_b = hand_a.hand_str[i], hand_b.hand_str[i]
        if card_a != card_b:
            return CARD_VALUE[card_b] - CARD_VALUE[card_a]


def solution(lines: list[str]):
    hands_arr = [Hand(hand_str, bid) for (hand_str, bid) in [line.split() for line in lines]]
    print(hands_arr)
    
    hands_arr.sort(key=cmp_to_key(compare_hands), reverse=True)
    print(hands_arr)

    total_win = 0
    for (rank, hand) in enumerate(hands_arr):
        total_win += ((rank + 1) * hand.bid)
    
    print(total_win)


lines = read_input_file(file_path="input.txt")
solution(lines)