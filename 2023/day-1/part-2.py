TEXT_DIGIT_MAP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


MIN_DIGIT_TEXT_LEN = 3


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_first_calibration_value(line: str):
    substr = ''
    for char in line:
        if char.isdigit():
            return char
        
        substr += char
        if len(substr) >= MIN_DIGIT_TEXT_LEN:
            for key, value in TEXT_DIGIT_MAP.items():
                if key in substr:
                    return value


def get_last_calibration_value(line: str):
    substr: str = ''
    for char in line[::-1]:
        if char.isdigit():
            return char
    
        substr = char + substr
        if len(substr) >= MIN_DIGIT_TEXT_LEN:
            for key, value in TEXT_DIGIT_MAP.items():
                if key in substr:
                    return value


def solution(lines: list[str]):
    total_sum = 0
    for line in lines:
        first_value = get_first_calibration_value(line)
        last_value = get_last_calibration_value(line)
        total_sum += int(f'{first_value}{last_value}')
    print(total_sum)



lines = read_input_file(file_path="input.txt")
solution(lines)