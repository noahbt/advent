#!/usr/bin/env python3

TEST_INPUT = [
    "123 328  51 64 ",
    "45 64  387 23 ",
    "6 98  215 314",
    "*   +   *   +  "
]

def main():
    with open('input6.txt', 'r') as f:
        data = f.readlines()
    # data = TEST_INPUT
    total = calculate_expression_sum(data)
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

if __name__ == "__main__":
    main()
