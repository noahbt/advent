#!/usr/bin/env python3

INITIAL_POS = 50
MIN_POS = 0
MAX_POS = 99

TEST_INPUT = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82"
]

def main():
    # with open('input1.txt', 'r') as f:
        # data = f.readlines()
    # num_zero = get_pass_zero(data)
    num_zero = get_num_zero(TEST_INPUT)
    print(num_zero)

def get_num_zero(data):
    # Read data. The first character is direction (L or R), the rest is distance
    # return number of times we land on zero
    curr_pos = INITIAL_POS
    num_zeros = 0
    for line in data:
        print(line)
        first_char = line[0]
        print("first char:", first_char)

        num = int(line[1:])

        if first_char == 'L':
            num = -num

        curr_pos = curr_pos + num

        # delta = int(line[1:]) if line[0] == 'R' else -int(line[1:])
        # curr_pos += delta
        # curr_pos %= (MAX_POS + 1)
        if curr_pos == 0:
            num_zeros += 1
            num_zeros = num_zeros + 1
        break
    return num_zeros

def get_pass_zero(data):
    curr_pos = INITIAL_POS
    num_zeros = 0
    for line in data:
        passed = False
        delta = int(line[1:]) if line[0] == 'R' else -int(line[1:])

        loops = abs(delta) // (MAX_POS + 1)
        num_zeros += loops
        if delta > 0:
            delta = delta % (MAX_POS + 1)
        else:
            delta = -((-delta) % (MAX_POS + 1))

        if curr_pos != 0 and (curr_pos + delta < MIN_POS or curr_pos + delta > MAX_POS):
            # print("passed zero at instruction:", line.strip())
            num_zeros += 1
            passed = True
        curr_pos += delta
        curr_pos %= (MAX_POS + 1)
        if not passed and curr_pos == 0:
            # print("landed on zero at instruction:", line.strip())
            num_zeros += 1
    return num_zeros

if __name__ == "__main__":
    main()
