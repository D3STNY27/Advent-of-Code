def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_first_calibration_value(line: str):
    for char in line:
        if char.isdigit():
            return char


def get_last_calibration_value(line: str):
    for char in line[::-1]:
        if char.isdigit():
            return char


def solution(lines: list[str]):
    total_sum = 0
    for line in lines:
        first_value = get_first_calibration_value(line)
        last_value = get_last_calibration_value(line)
        total_sum += int(f'{first_value}{last_value}')
    print(total_sum)



lines = read_input_file(file_path="input.txt")
solution(lines)