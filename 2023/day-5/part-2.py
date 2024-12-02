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


def get_mapped_ranges(
    key_start: int,
    key_range: int,
    maps_arr: list[list[tuple]],
    map_idx: int
):
    key_end = (key_start + key_range - 1)
    ranges = []

    for (dst_start, src_start, range_len) in maps_arr[map_idx]:
        src_end = (src_start + range_len - 1)

        if key_start >= src_start and key_end <= src_end:
            ranges.append((dst_start + (key_start - src_start), key_range))
        elif key_start < src_start and (src_start <= key_end <= src_end):
            ranges.append((dst_start + (key_start - src_start), key_range))
        elif key_end > src_end and (src_start <= key_start <= src_end):
            print('overlap end')
        else:
            print('partial contains')



def solution(lines: list[str]):
    seeds_ranges = list(map(int, lines[0].split(':')[1].strip().split(' ')))
    seeds = []

    for i in range(0, len(seeds_ranges), 2):
        seed_start, seed_range = seeds_ranges[i], seeds_ranges[i+1]
        seeds.append((seed_start, seed_range))
    
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
    
    for (seed_start, seed_range) in seeds:
        next_map = get_mapped_ranges(seed_start, seed_range, maps_arr, 0)


lines = read_input_file(file_path="input.txt")
solution(lines)