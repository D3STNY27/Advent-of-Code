stack = [
    [],
    ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
    ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
    ['C', 'V', 'S', 'H'],
    ['H', 'F', 'G'],
    ['P', 'G', 'J', 'B', 'Z'],
    ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
    ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
    ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
    ['W', 'P', 'V', 'M', 'B', 'H']
]

with open('input.txt', 'r') as file_in:
    lines = [line.strip().split() for line in file_in.readlines()[10:]]
    
    for line in lines:
        count, src, dst = [int(x) for x in line if x.isdigit()]

        temp_stack = []
        while count:
            top = stack[src].pop()
            temp_stack.append(top)
            count -= 1
        
        while temp_stack:
            top = temp_stack.pop()
            stack[dst].append(top)

        
for i in range(len(stack)):
    try:
        print(stack[i][-1])
    except:
        x = 1