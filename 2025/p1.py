#!/usr/bin/env python

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
    with open('input1', 'r') as f:
        data = f.readlines()
    num_zero = get_num_zero(data)
    # num_zero = get_num_zero(TEST_INPUT)
    print(num_zero)

def get_num_zero(data):
    curr_pos = INITIAL_POS
    zeros = 0
    for line in data:
        passed = False
        delta = int(line[1:]) if line[0] == 'R' else -int(line[1:])

        loops = abs(delta) // (MAX_POS + 1)
        zeros += loops
        if delta > 0:
            delta = delta % (MAX_POS + 1)
        else:
            delta = -((-delta) % (MAX_POS + 1))

        if curr_pos != 0 and (curr_pos + delta < MIN_POS or curr_pos + delta > MAX_POS):
            # print("passed zero at instruction:", line.strip())
            zeros += 1
            passed = True
        curr_pos += delta
        curr_pos %= (MAX_POS + 1)
        if not passed and curr_pos == 0:
            # print("landed on zero at instruction:", line.strip())
            zeros += 1
    return zeros

if __name__ == "__main__":
    main()
