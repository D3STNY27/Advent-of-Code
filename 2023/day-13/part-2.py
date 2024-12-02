import os
import numpy as np

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines] + ['']


def calculate_count(grid: np.ndarray):
    R, C = grid.shape
    
    mirror_columns, mirror_rows = [], []
    smudge_columns, smudge_rows = [], []

    # Find Vertical Mirrors
    for col in range(C-1):
        num_diff = 0
        mirror_status = True
        prev_idx, next_idx = (col + 1, col)

        while True:
            prev_idx, next_idx = (prev_idx - 1, next_idx + 1)
            if prev_idx < 0 or next_idx >= C:
                break
        
            if not np.array_equal(grid[:, prev_idx], grid[:, next_idx]):
                num_diff += 1
                if num_diff >= 2:
                    mirror_status = False
                    break
                
                idx_diff = np.where(grid[:, prev_idx] != grid[:, next_idx])[0]
                if len(idx_diff) != 1:
                    mirror_status = False
                    break

                if grid[:, prev_idx][idx_diff][0]==grid[:, next_idx][idx_diff][0]:
                    mirror_status = False
                    break
        
        if mirror_status:
            if num_diff==0:
                mirror_columns.append(col)
            else:
                smudge_columns.append(col)
    

    # Find Horizontal Mirrors
    for row in range(R-1):
        num_diff = 0
        mirror_status = True
        prev_idx, next_idx = (row + 1, row)

        while True:
            prev_idx, next_idx = (prev_idx - 1, next_idx + 1)
            if prev_idx < 0 or next_idx >= R:
                break
        
            if not np.array_equal(grid[prev_idx, :], grid[next_idx, :]):
                num_diff += 1
                if num_diff >= 2:
                    mirror_status = False
                    break

                idx_diff = np.where(grid[prev_idx, :] != grid[next_idx, :])[0]
                if len(idx_diff) != 1:
                    mirror_status = False
                    break

                if grid[prev_idx, :][idx_diff][0]==grid[next_idx, :][idx_diff][0]:
                    mirror_status = False
                    break
        
        if mirror_status:
            if num_diff==0:
                mirror_rows.append(row)
            else:
                smudge_rows.append(row)
    
    return (
        sum(smudge_columns) + len(smudge_columns),
        sum(smudge_rows) + len(smudge_rows)
    )

def solution(lines: list[str]):
    grid_arr, summarize = [], 0

    for line in lines:
        if not line:
            grid = np.array(grid_arr)
            grid_arr.clear()

            vertical_mirrors, horizontal_mirrors = calculate_count(grid)
            summarize += (vertical_mirrors + 100*horizontal_mirrors)
            continue

        grid_arr.append([1 if c=='#' else 0 for c in line])
    
    print(summarize)

lines = read_input_file(file_path="input.txt")
solution(lines)