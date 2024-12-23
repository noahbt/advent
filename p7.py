#!/Users/noahthomas/Code/advent/venv/bin/python
import numpy as np

FNAME = 'input7'

def _main():
    # Read
    with open(FNAME, 'r') as fp:
        lines = fp.readlines()
    
    result = calibrate(lines)
    # Output result
    print(f'Part 1: Total calibration result: {result}')


def calibrate(lines):
    cal_result = 0
    for line in lines:
        test_val = int(line.split(':')[0])
        nums = [int(x) for x in line.split(':')[1].split(' ')]
        line_result = analyze_line(test_val, nums)
        cal_result += line_result


def analyze_line(test_val, nums):
    # determine if operators + and * can be combined to acheive a truthy equation
    # return test_val if truthy, else 0
    total_operators = len(nums) - 1
    if total_operators > 0:
        return test_val
    # bin(4) = '0b01'
    return 0


if __name__ == '__main__':
    _main()
