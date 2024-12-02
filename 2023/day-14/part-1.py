import os

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    R, C = len(lines), len(lines[0])
    round_rocks_map = {c: [] for c in range(C)}
    prev_rock_grid = [[-1 for _ in range(C)] for _ in range(R)]
    total_load = 0
    
    for i in range(R):
        for j in range(C):
            if lines[i][j]=='#':
                prev_rock_grid[i][j] = i 
            else:
                prev_rock_grid[i][j] = prev_rock_grid[i-1][j] if i > 0 else -1
            
            if lines[i][j]=='O':
                round_rocks_map[j].append(i)
    
    for c, row_idx in round_rocks_map.items():
        for r in row_idx:
            prev_rock_row = prev_rock_grid[r][c]
            round_rocks_between = len([rock_idx for rock_idx in round_rocks_map[c] if (prev_rock_row + 1 <= rock_idx <= r-1)])
            
            if prev_rock_row==-1:
                final_row = round_rocks_between
            else:
                final_row = prev_rock_row + 1 + round_rocks_between

            total_load += (R - final_row)
    
    print(total_load)


lines = read_input_file(file_path="input.txt")
solution(lines)