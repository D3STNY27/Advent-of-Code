import os
from enum import Enum
from pprint import pprint

os.system('cls')


class Signal(Enum):
    HIGH = True
    LOW = False


class Module:
    def __init__(self, name: str, attached_modules: list):
        self.name = name
        self.attached_modules = attached_modules


class Broadcaster(Module):
    def __init__(self, attached_modules: list):
        super().__init__('broadcaster', attached_modules)
    
    def process_signal(self, signal: Signal, sent_by: str):
        return [(module, self.name, signal) for module in self.attached_modules]
    
    def __repr__(self):
        return f'Broadcaster: {self.attached_modules}'


class FlipFlop(Module):
    def __init__(self, name: str, attached_modules: list):
        super().__init__(name, attached_modules)
        self.off = True

    def process_signal(self, signal: Signal, sent_by: str):
        if signal==Signal.HIGH:
            return []
        
        self.off = not self.off
        if self.off:
            return [(module, self.name, Signal.LOW) for module in self.attached_modules]
        else:
            return [(module, self.name, Signal.HIGH) for module in self.attached_modules]
    
    def __repr__(self):
        return f'Flip-Flip ({self.name}): {self.attached_modules}, Off={self.off}'


class Conjunction(Module):
    def __init__(self, name: str, attached_modules: list):
        super().__init__(name, attached_modules)
        self.input_history = {}
    
    def create_input_history(self, input_module):
        if input_module in self.input_history:
            return
        
        self.input_history[input_module] = Signal.LOW

    def process_signal(self, signal: Signal, sent_by: str):
        self.input_history[sent_by] = signal

        if all([value==Signal.HIGH for key, value in self.input_history.items()]):
            return [(module, self.name, Signal.LOW) for module in self.attached_modules]
        return [(module, self.name, Signal.HIGH) for module in self.attached_modules]
    
    def __repr__(self):
        return f'Conjunction ({self.name}): {self.attached_modules}, History={self.input_history}'


class Unknown(Module):
    def __init__(self, name: str, attached_modules: list = []):
        super().__init__(name, attached_modules)
    
    def process_signal(self, signal: Signal, sent_by: str):
        return []

    def __repr__(self):
        return f'Unknown ({self.name})'


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    NUM_BUTTON_PRESS = 10000000
    module_map = {}
    all_modules = set()

    # Create Module and Object Map
    for line in lines:
        tokens = line.split()
        module, attached_modules_raw = tokens[0], tokens[2:]
        attached_modules = [module.rstrip(',') for module in attached_modules_raw]

        for attached_module in attached_modules:
            all_modules.add(attached_module)
        
        if module=='broadcaster':
            module_map[module] = Broadcaster(attached_modules)
            all_modules.add(module)
            continue
    
        module_type, module_name = module[0], module[1:]
        all_modules.add(module_name)
        if module_type=='%':
            module_map[module_name] = FlipFlop(module_name, attached_modules)
        else:
            module_map[module_name] = Conjunction(module_name, attached_modules)
    
    # Add Unknown Modules
    for module in all_modules:
        if module in module_map:
            continue
        module_map[module] = Unknown(module)

    # Add Inputs For Conjunction Modules
    for module, module_obj in module_map.items():
        for attached_module in module_obj.attached_modules:
            attached_module_obj = module_map[attached_module]
            if isinstance(attached_module_obj, Conjunction):
                attached_module_obj.create_input_history(module)
    
    # Simulate
    for _ in range(NUM_BUTTON_PRESS):
        queue = [('broadcaster', None, Signal.LOW)]
        while queue:
            module, sent_by_module, signal = queue[0]
            queue = queue[1:]

            module_obj = module_map[module]
            for output in module_obj.process_signal(signal, sent_by_module):
                queue.append(output)
        
        print(module_map['tc'].input_history)
    


lines = read_input_file(file_path="input.txt")
solution(lines)