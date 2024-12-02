import os
from enum import Enum
from pprint import pprint

os.system('cls')


EVAL_MAP = {
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b 
}


class Part:
    def __init__(self, part: tuple) -> None:
        self.x, self.m, self.a, self.s = part
    
    def get_value(self, category: str):
        return getattr(self, category)

    def get_total(self) -> int:
        return (self.x + self.m + self.a + self.s)
    
    def __repr__(self):
        return f'part(x={self.x}, m={self.m}, a={self.a}, s={self.s})'


class Workflow:
    def __init__(self, name: str, rules: str):
        self.name = name
        self.rules = rules.split(',')
    

    def evaluate_part(self, part: Part):
        for rule in self.rules:
            if any([operator in rule for operator in EVAL_MAP.keys()]):
                condition, result = rule.split(':')
                category, operator, b = condition[0], condition[1], int(condition[2:])
                if EVAL_MAP[operator](part.get_value(category), b):
                    return result
        return rule
    

    def __repr__(self):
        return f'workflow(name={self.name}, rules={self.rules})'
    

def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_clean_part_str(part_str: str):
    clean_str = ''
    for c in part_str:
        if c==',' or c.isdigit():
            clean_str += c
    return tuple(map(int, clean_str.split(',')))


def get_clean_workflow(workflow_str: str) -> tuple:
    split_idx = workflow_str.index('{')
    workflow_name, workflow_rules = workflow_str[:split_idx], workflow_str[split_idx+1:-1]
    return workflow_name, workflow_rules


def solution(lines: list[str]):
    split_line = lines.index('')
    workflows_raw, parts_raw = lines[:split_line], lines[split_line+1:]

    workflow_map = {}
    total_accept_sum = 0

    for workflow_str in workflows_raw:
        name, rules = get_clean_workflow(workflow_str)
        workflow_map[name] = Workflow(name, rules)
    
    for part_str in parts_raw:
        part_obj = Part(get_clean_part_str(part_str))

        result = None
        current_workflow = 'in'
        while True:
            result = workflow_map[current_workflow].evaluate_part(part_obj)
            if result=='A' or result=='R':
                break
            current_workflow = result
        
        if result=='A':
            total_accept_sum += part_obj.get_total()
        
    print(total_accept_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)