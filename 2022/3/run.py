priority_list = []
common_map = {}
total_sum = 0

lower_case = list('abcdefghijklmnopqrstuvwxyz')
upper_case = [c.upper() for c in lower_case]

priority_map = {lower_case[i]: i+1 for i in range(len(lower_case))}
priority_map |= {upper_case[i]: i+27 for i in range(len(upper_case))}

with open('input.txt', 'r') as file_in:
    lines = [line.strip() for line in file_in.readlines()]
    for i in range(0, len(lines), 3):
        first, second, third = lines[i:i+3]
        
        for c in (lower_case + upper_case):
            if c in first and c in second and c in third:
                total_sum += priority_map[c]

print(total_sum)