max_calories = float('-inf')
calories = []

elf_num = 1
with open('input.txt', 'r') as file_in:
    lines = [line.strip() for line in file_in.readlines()] + ['']
    current_sum = 0

    for line in lines:
        if line=='':
            if current_sum > max_calories:
                max_calories = current_sum

            calories.append(current_sum)
            current_sum = 0
            elf_num += 1
        else:
            current_sum += int(line)

print(sum(sorted(calories)[-1:-4:-1]))