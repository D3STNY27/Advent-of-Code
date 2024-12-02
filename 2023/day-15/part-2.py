import os

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_label_hash(label: str):
    current_value = 0
    for c in label:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def solution(lines: list[str]):
    box_map, lens_map = {}, {}

    for string in lines[0].split(','):
        if '-' in string:
            label = string[:-1]
            label_hash = get_label_hash(label)

            if label_hash in box_map:
                try:
                    box_map[label_hash].pop(box_map[label_hash].index(label))
                except:
                    pass

        else:
            label, focal_length = string.split('=')
            label_hash = get_label_hash(label)
            lens_map[label] = focal_length

            if label_hash not in box_map:
                box_map[label_hash] = [label]
            else:
                if label not in box_map[label_hash]:
                    box_map[label_hash] = box_map[label_hash] + [label]
    
    total_power = 0
    for box, lenses in box_map.items():
        if not lenses:
            continue
    
        for index, lense in enumerate(lenses):
            total_power += ((box + 1) * (index + 1) * int(lens_map[lense]))
    
    print(total_power)


lines = read_input_file(file_path="input.txt")
solution(lines)