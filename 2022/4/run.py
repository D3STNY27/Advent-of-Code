count = 0

with open('input.txt', 'r') as file_in:
    lines = [line.strip().split(',') for line in file_in.readlines()]
    lines = [line[0].split('-') + line[1].split('-') for line in lines]

    for a, b, c, d in lines:
        a, b, c, d = int(a), int(b), int(c), int(d)
        
        if d < a:
            count += 1
            continue
    
        if c > b:
            count += 1
            continue

print(count)