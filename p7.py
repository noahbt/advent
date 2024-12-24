#!/Users/noahthomas/Code/advent/venv/bin/python

FNAME = 'input7'

def _main():
    # Read
    with open(FNAME, 'r') as fp:
        lines = fp.readlines()
    # solve
    result, result_2 = calibrate(lines)
    # Output result
    print(f'Part 1: Total calibration result: {result}')
    print(f'Part 2: Total calibration result 2: {result_2}')



def calibrate(lines):
    cal_result, cal_result_2 = 0, 0
    for i, line in enumerate(lines):
        test_val = int(line.split(':')[0])
        nums = [int(x) for x in line.split(':')[1].strip().split(' ')]
        line_result = analyze_line(test_val, nums)
        line_result_2 = analyze_line_2(test_val, nums)
        cal_result += line_result
        cal_result_2 += line_result_2
        print(f'{i+1:03d}/850 - [{line.strip()}] - {line_result}, {line_result_2}')
    return cal_result, cal_result_2


def analyze_line(test_val, nums):
    """
    Determine if operators + and * can be combined to acheive a truthy equation
    return test_val if truthy, else 0
    """
    total_operators = len(nums) - 1
    operator_combos = pow(2, total_operators)
    for i in range(operator_combos):
        operator_str = f'{i:>016b}'[::-1]
        res = nums[0]
        for j, num in enumerate(nums[1:]):
            c = operator_str[j]
            res = res * num if c == '1' else res + num
            if res > test_val:
                break
        if res == test_val:
            return res
    return 0

def analyze_line_2(test_val, nums):
    """
    Determine if operators + and * can be combined to acheive a truthy equation
    return test_val if truthy, else 0
    """
    total_operators = len(nums) - 1
    operator_combos = pow(3, total_operators)
    for i in range(operator_combos):
        operator_str = f'{int(_ternary(i)):>016d}'[::-1]
        res = nums[0]
        for j, num in enumerate(nums[1:]):
            c = operator_str[j]
            if c == '0':
                res += num
            elif c == '1':
                res *= num
            else:
                res = int(f'{res}{num}')
            if res > test_val:
                break
        # print(operator_str, res)
        if res == test_val:
            return res
    return 0


def _ternary(n):
    # convert int to ternary string
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


if __name__ == '__main__':
    _main()
