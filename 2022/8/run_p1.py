grid = []

with open('input.txt', 'r') as file_in:
    for line in file_in.readlines():
        line = [int(x) for x in list(line.strip())]
        grid.append(line)

WIDTH = len(grid[0])
HEIGHT = len(grid)

VISIBLE_BOUNDRY = (2 * WIDTH) + (2 * (HEIGHT-2))

visible_count = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        tree = grid[i][j]

        if tree > max(grid[i][:j]):
            print(i, j, tree, 'left')
            visible_count += 1
            continue
        if tree > max(grid[i][j+1:]):
            print(i, j, tree, 'right')
            visible_count += 1
            continue
        if tree > max([row[j] for row in grid[:i]]):
            print(i, j, tree, 'top')
            visible_count += 1
            continue
        if tree > max([row[j] for row in grid[i+1:]]):
            print(i, j, tree, 'bottom')
            visible_count += 1
            continue

print(VISIBLE_BOUNDRY, visible_count, VISIBLE_BOUNDRY + visible_count)