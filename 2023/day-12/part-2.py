import os
from functools import cache

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


@cache
def get_max_groups(sub_record: str):
    max_groups = 0
    prev_spring = '.'

    for c in sub_record:
        if c=='#':
            if prev_spring=='.':
                max_groups += 1
            prev_spring = c
        else:
            if prev_spring=='#':
                prev_spring = '.'
            else:
                max_groups += 1
                prev_spring = '#'
    
    return max_groups


@cache
def generate_records(records: tuple, info: tuple):
    if not records:
        if info:
            return 0
        return 1

    max_groups, len_sum, match_groups = 0, 0, 0
    partition, position = -1, -1

    for idx, record in enumerate(records):
        if (position := record.find('?')) >= 0:
            partition = idx
            break

        if not info:
            return 0
        
        if idx >= len(info):
            return 0
        
        if idx < len(info):
            if (len(record) != info[idx]):
                return 0
            match_groups += 1

        max_groups += 1
        len_sum += len(record)
    
    if partition != -1:
        for i in range(partition, len(records)):
            if records[i].find('?') >= 0:
                max_groups += get_max_groups(records[i])
            else:
                max_groups += 1
    
    if max_groups < len(info):
        return 0

    if partition==position==-1:
        if match_groups==len(records)==len(info):
            return 1
        return 0
    
    record_sub_a = []

    if (r := records[partition][:position])!='':
        record_sub_a.append(r)
    
    if (r := records[partition][position+1:])!='':
        record_sub_a.append(r)

    record_sub_b = records[partition][:position] + '#' + records[partition][position+1:]

    return (
        generate_records(tuple(record_sub_a) + records[partition+1:], info[match_groups:]) +
        generate_records((record_sub_b,) + records[partition+1:], info[match_groups:])
    )
    

def solution(lines: list[str]):
    total_count = 0
    multiplier = 5
    for line in lines:
        records, info_str = line.split()
        info = tuple(map(int, info_str.split(','))) * multiplier
        records = '?'.join([records for _ in range(multiplier)])
        
        records_split = tuple(r for r in records.split('.') if r!='')
        count = generate_records(records_split, info)
        total_count += count
    
    print(total_count)

lines = read_input_file(file_path="input.txt")
solution(lines)