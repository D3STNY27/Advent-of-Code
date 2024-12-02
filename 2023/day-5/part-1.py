import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_mapped_value(key: int, maps_arr: list[list[tuple]], map_idx: int):
    for (dst_start, src_start, range_len) in maps_arr[map_idx]:
        if key >= src_start and key < (src_start + range_len):
            offset = (key - src_start)
            return (dst_start + offset)
    return key


def solution(lines: list[str]):
    seeds = list(map(int, lines[0].split(':')[1].strip().split(' ')))
    maps_arr, current_map = [], []

    for line in lines[2:] + ['']:
        if 'map' in line:
            continue

        if line=='':
            maps_arr.append(current_map.copy())
            current_map.clear()
            continue
    
        tokens = tuple(map(int, line.split()))
        current_map.append(tokens)
    
    min_location = float('inf')
    for seed in seeds:
        soil = get_mapped_value(seed, maps_arr, 0)
        fertilizer = get_mapped_value(soil, maps_arr, 1)
        water = get_mapped_value(fertilizer, maps_arr, 2)
        light = get_mapped_value(water, maps_arr, 3)
        temp = get_mapped_value(light, maps_arr, 4)
        humidity = get_mapped_value(temp, maps_arr, 5)
        location = get_mapped_value(humidity, maps_arr, 6)
        if location < min_location:
            min_location = location
    
    print(min_location)


lines = read_input_file(file_path="input.txt")
solution(lines)