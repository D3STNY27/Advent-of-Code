import os

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def expand_grid(galaxy_arr: list, idx_arr: list, dir: int):
    expanded_arr = []
    for (x, y) in galaxy_arr:
        if dir==0:
            idx_offset = len([i for i in idx_arr if i < x]) * 999999
            expanded_arr.append((x + idx_offset, y))
        else:
            idx_offset = len([i for i in idx_arr if i < y]) * 999999
            expanded_arr.append((x, y + idx_offset))
    return expanded_arr
        

def solution(lines: list[str]):
    empty_rows, empty_cols, galaxy_arr = [], [], []
    grid = [list(line) for line in lines]
    r, c = len(grid), len(grid[0])

    column_count = {j: 0 for j in range(c)}
    for i in range(r):
        if grid[i].count('#')==0:
            empty_rows.append(i)
        
        for j in range(c):
            if grid[i][j]=='#':
                galaxy_arr.append((i, j))
                column_count[j] += 1

    empty_cols = [key for (key, val) in column_count.items() if val==0]
    
    # Expand Rows and Columns
    galaxy_arr = expand_grid(galaxy_arr, empty_rows, 0)
    galaxy_arr = expand_grid(galaxy_arr, empty_cols, 1)
    
    total_distance = 0
    for i in range(len(galaxy_arr)-1):
        for j in range(i+1, len(galaxy_arr)):
            (x1, y1), (x2, y2) = galaxy_arr[i], galaxy_arr[j]
            distance = abs(y2 - y1) + abs(x2 - x1)
            total_distance += distance
    
    print(total_distance)


lines = read_input_file(file_path="input.txt")
solution(lines)