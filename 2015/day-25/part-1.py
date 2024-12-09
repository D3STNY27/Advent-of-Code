def get_code_number(r, c):
    x = (((r**2 - r) / 2) + 1)
    y = x + ((c**2 / 2) + (((2*r + 1) * c) / 2) - r - 1)
    return int(y - c + 1)


def solution(row, column):
    n = get_code_number(row, column)
    
    code = 20151125
    for _ in range(n-1):
        code = (code * 252533) % 33554393
    
    print(code)
    


# row 2981, column 3075
solution(row=2981, column=3075)