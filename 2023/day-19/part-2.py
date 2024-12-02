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
    
    def get_rules(self) -> list:
        rule_list = []
        for rule in self.rules:
            if any([operator in rule for operator in EVAL_MAP.keys()]):
                condition, result = rule.split(':')
                rule_list.append((True, condition, result))
                continue

            rule_list.append((False, None, rule))
        return rule_list
    

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


def get_clean_workflow(workflow_str: str) -> tuple:
    split_idx = workflow_str.index('{')
    workflow_name, workflow_rules = workflow_str[:split_idx], workflow_str[split_idx+1:-1]
    return workflow_name, workflow_rules


def caculate_possible_solutions(solution: list):
    category_range = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }

    for (condition, evaluation) in solution:
        category, operator, value = condition[0], condition[1], int(condition[2:])
        min_val, max_val = category_range[category]

        if operator=='<':
            if evaluation:
                category_range[category] = (min_val, min(max_val, value-1))
            else:
                category_range[category] = (max(min_val, value), max_val)
        else:
            if evaluation:
                category_range[category] = (max(min_val, value+1), max_val)
            else:
                category_range[category] = (min_val, min(max_val, value))

    total_sum = 1
    for key, (min_v, max_v) in category_range.items():
        total_sum *= (max_v - min_v + 1)
    return total_sum


def solution(lines: list[str]):
    split_line = lines.index('')
    workflows_raw = lines[:split_line]

    workflow_map = {}

    for workflow_str in workflows_raw:
        name, rules = get_clean_workflow(workflow_str)
        workflow_map[name] = Workflow(name, rules)
    
    sol_set = []
    queue = [('in', [])]

    while queue:
        workflow, conditions = queue[0]
        queue = queue[1:]

        if workflow=='A':
            sol_set.append(conditions)
            continue
    
        if workflow=='R':
            continue
    
        rules = workflow_map[workflow].get_rules()
        for i in range(len(rules)):
            conditions_new = conditions.copy()
            operator_condition, current_condition, current_result = rules[i]
            condition_states = [(rules[j][1], False) for j in range(0, i) if rules[j][0]]
            if operator_condition:
                condition_states += [(current_condition, True)]
            conditions_new.extend(condition_states)
            queue.append((current_result, conditions_new))
    
    total_solutions = 0
    for sol in  sol_set:
        total_solutions += caculate_possible_solutions(sol)
    print(total_solutions)


lines = read_input_file(file_path="input.txt")
solution(lines)