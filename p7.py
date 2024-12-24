#!/Users/noahthomas/Code/advent/venv/bin/python

FNAME = 'input7'

def _main():
    # Read
    with open(FNAME, 'r') as fp:
        lines = fp.readlines()
    # solve
    result = calibrate(lines)
    # Output result
    print(f'Part 1: Total calibration result: {result}')


def calibrate(lines):
    cal_result = 0
    for i, line in enumerate(lines):
        test_val = int(line.split(':')[0])
        nums = [int(x) for x in line.split(':')[1].strip().split(' ')]
        line_result = analyze_line(test_val, nums)
        cal_result += line_result
        print(f'{i+1:03d}/850 - [{line.strip()}] - {line_result}')
    return cal_result


def analyze_line(test_val, nums):
    """
    Determine if operators + and * can be combined to acheive a truthy equation
    return test_val if truthy, else 0
    """
    total_operators = len(nums) - 1
    operator_combos = pow(2, total_operators)
    res = 0
    for i in range(operator_combos):
        operator_str = f'{i:>016b}'[::-1]
        res = nums[0]
        for j, num in enumerate(nums[1:]):
            c = operator_str[j]
            if c == '1':
                res *= num
            else:
                res += num
            if res > test_val:
                break
        if res == test_val:
            return res
    return 0


if __name__ == '__main__':
    _main()
