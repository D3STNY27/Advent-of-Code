with open('input.txt', 'r') as file_in:
    lines = [tuple(line.strip().split()) for line in file_in.readlines()]

    X = 1
    cycles = [X]
    for (cmd, *value) in lines:
        if cmd=='noop':
            cycles.append(X)
        else:
            increment = int(value[0])
            cycles.append(X)
            X += increment
            cycles.append(X)

SPECIAL_CYCLES = [20, 60, 100, 140, 180, 220]

total_sum = 0
for idx in SPECIAL_CYCLES:
    total_sum += (idx * cycles[idx-1])

print(total_sum)

crt_out = ''
for idx in range(0, len(cycles)-1):
    if (idx % 40) in [cycles[idx]-1, cycles[idx], cycles[idx]+1]:
        crt_out += '#'
    else:
        crt_out += '.'

for i in range(0, len(crt_out), 40):
    print(crt_out[i:i+40])