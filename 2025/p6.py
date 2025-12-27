#!/usr/bin/env python3

TEST_INPUT = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  "
]

def main():
    with open('input6.txt', 'r') as f:
        data = f.readlines()
    # data = TEST_INPUT
    total = calculate_expression_sum2(data)
    print(f"Total sum of expressions: {total}")

def calculate_expression_sum(data):
    # read in the data
    # The last line is the operators line
    # The other lines need to be operated on column-wise
    operators_line = data[-1].strip().split()
    result_arr = []
    for o in operators_line:
        result_arr.append(0 if o == '+' else 1)
    for line in data[:-1]:
        numbers = line.strip().split()
        for i in range(len(numbers)):
            num = int(numbers[i])
            operator = operators_line[i]
            if operator == '*':
                result_arr[i] *= num
            elif operator == '+':
                result_arr[i] += num
            else:
                print(f"Unknown operator: {operator}")
    total_sum = sum(result_arr)
    return total_sum

def calculate_expression_sum2(data):
    # same thing as last time, except the numbers are top down instead of left to right
    line_length = len(data[0].strip())
    operators_line = data[-1].strip().split()
    result_arr = []

    op_i = 0
    col = 0
    # read columns until you get all spaces, then perform the operation on the resulting numbers
    # each column is a number
    numbers = []
    while col < line_length:
        num_str = ''
        for row in range(len(data) - 1):
            char = data[row][col]
            if char != ' ':
                num_str += char
        if num_str == '':
            # perform operation on numbers and add this to the the result array
            result = calculate_result(numbers, operators_line[op_i])
            result_arr.append(result)
            op_i += 1
            numbers = []
        else:
            numbers.append(int(num_str))
        col += 1
    result = calculate_result(numbers, operators_line[op_i])
    result_arr.append(result)
    total_sum = sum(result_arr)
    assert len(result_arr) == len(operators_line)
    return total_sum

def calculate_result(numbers, operator):
    if operator == '*':
        prod = 1
        for n in numbers:
            prod *= n
        return prod
    elif operator == '+':
        return sum(numbers)

if __name__ == "__main__":
    main()
