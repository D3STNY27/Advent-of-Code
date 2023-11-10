grid = []

with open('input.txt', 'r') as file_in:
    for line in file_in.readlines():
        line = [int(x) for x in list(line.strip())]
        grid.append(line)

WIDTH = len(grid[0])
HEIGHT = len(grid)

def get_visible(tree, i, j, grid, type):
    #print(f'[DEBUG] - {type}')
    count = 0
    while True:
        if type==0:
            i, j = i-1, j
        elif type==1:
            i, j = i, j-1
        elif type==2:
            i, j = i+1, j
        else:
            i, j = i, j+1
        
        count += 1
        if i<=0 or i>=HEIGHT-1 or j<=0 or j>=WIDTH-1:
            break
    
        #print(i, j)
        if grid[i][j] >= tree:
            break

    return count

max_score = float('-inf')
for i in range(HEIGHT):
    for j in range(WIDTH):
        v_top = get_visible(grid[i][j], i, j, grid, 0)
        v_left = get_visible(grid[i][j], i, j, grid, 1)
        v_bottom = get_visible(grid[i][j], i, j, grid, 2)
        v_right = get_visible(grid[i][j], i, j, grid, 3)

        score = (v_bottom * v_left * v_top * v_right)
        max_score = score if score > max_score else max_score

print(max_score)