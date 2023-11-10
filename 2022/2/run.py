total_score = 0

with open('input.txt', 'r') as file_in:
    lines = [line.strip().split() for line in file_in.readlines()]
    for line in lines:
        elf, player = line
        
        if player=='X':
            total_score += 0
            if elf=='A':
                total_score += 3
            elif elf=='B':
                total_score += 1
            else:
                total_score += 2

        elif player=='Y':
            total_score += 3
            if elf=='A':
                total_score += 1
            elif elf=='B':
                total_score += 2
            else:
                total_score += 3

        else:
            total_score += 6
            if elf=='A':
                total_score += 2
            elif elf=='B':
                total_score += 3
            else:
                total_score += 1

print(total_score)