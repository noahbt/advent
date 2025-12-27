#!/usr/bin/env python3

TEST_INPUT = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]

def main():
    with open('input3.txt', 'r') as f:
        data = f.readlines()
    # total_joltage = get_total_joltage(TEST_INPUT)
    total_joltage = get_total_joltage(data)
    print(f"Total joltage: {total_joltage}")

def get_total_joltage(data):
    total_joltage = 0
    for line in data:
        total_joltage += get_max_joltage2(line.strip())
    return total_joltage

def get_max_joltage(line):
    i, li = 0, 0
    l = int(line[i])
    while i < len(line) - 1:
        n = int(line[i])
        if n > l:
            l = n
            li = i
        i += 1
    i = li + 1
    r = int(line[i])
    while i < len(line):
        n = int(line[i])
        if n > r:
            r = n
        i += 1
    return l*10 + r

def get_max_joltage2(line):
    # This time it is an 12 digit number instead of a 2 digit number
    # find the largest 12 digit number that can be formed from the digits in the line
    # Take the example of "818181911112111"
    # The 9 is the largest, but there are not 11 digits to the right of it
    # So the first digit has to be in the first 4 digits
    # So we can have an iterator that grabs each digit in turn
    # The window should be 0 to 3, 1 to 4, ..., 11 to 14
    # The big input has longer line lengths
    digits = []
    last_index = 0
    i = 0
    len_line = len(line)
    len_digits = 12
    window_size = len_line - len_digits + 1
    while i < len_digits:
        max_digit = -1
        for j in range(last_index, i + window_size):
            n = int(line[j])
            if n > max_digit:
                max_digit = n
                last_index = j + 1
        digits.append(str(max_digit))
        i += 1
    return int(''.join(digits))

if __name__ == "__main__":
    main()
