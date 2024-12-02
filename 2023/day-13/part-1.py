import os
import numpy as np

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines] + ['']


def calculate_count(grid: np.ndarray):
    R, C = grid.shape
    
    check_columns, check_rows = [], []
    mirror_columns, mirror_rows = [], []

    # Check Possible Mirror Columns and Rows
    for i in range(C-1):
        if np.array_equal(grid[:,i], grid[:, i+1]):
            check_columns.append(i)
    
    for i in range(R-1):
        if np.array_equal(grid[i, :], grid[i+1, :]):
            check_rows.append(i)

    # Verify Vertical Mirror
    for col in check_columns:
        mirror_status = True
        prev_idx, next_idx = (col, col + 1)

        while True:
            prev_idx, next_idx = (prev_idx - 1, next_idx + 1)
            if prev_idx < 0 or next_idx >= C:
                break
        
            if not np.array_equal(grid[:, prev_idx], grid[:, next_idx]):
                mirror_status = False
                break
        
        if mirror_status:
            mirror_columns.append(col)
    
    # Verify Horizontal Mirror
    for row in check_rows:
        mirror_status = True
        prev_idx, next_idx = (row, row + 1)

        while True:
            prev_idx, next_idx = (prev_idx - 1, next_idx + 1)
            if prev_idx < 0 or next_idx >= R:
                break
        
            if not np.array_equal(grid[prev_idx, :], grid[next_idx, :]):
                mirror_status = False
                break
        
        if mirror_status:
            mirror_rows.append(row)
    
    return (
        sum(mirror_columns) + len(mirror_columns),
        sum(mirror_rows) + len(mirror_rows)
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