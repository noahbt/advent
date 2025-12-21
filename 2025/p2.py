#!/usr/bin/env python

INITIAL_POS = 50
MIN_POS = 0
MAX_POS = 99

TEST_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,
    824824821-824824827,2121212118-2121212124"""

def main():
    with open('input2', 'r') as f:
        data = f.read()
    # invalid_ids = get_invalid_ids(TEST_INPUT)
    invalid_ids = get_invalid_ids(data)
    # print(invalid_ids)
    print(sum(invalid_ids))

def get_invalid_ids(data):
    duplicates = []
    ranges = data.split(',')
    for r in ranges:
        r = r.strip()
        start, end = r.split('-')
        for i in range(int(start), int(end) + 1):
            s = str(i)
            if has_repeat(s):
                # print(f"Duplicate found in range {r}: {s}")
                duplicates.append(i)
    return duplicates

def has_duplicate(s):
    length = len(s)
    half = length // 2
    first_half = s[:half]
    second_half = s[half:]
    return first_half == second_half

def has_repeat(s):
    # return true if any digits repeat
    # so 11, 111, 1212, 123123, 121212, 148914891489 are true
    # if set(s) == {s[0]}:
        # return True
    length = len(s)
    for size in range(1, length // 2 + 1):
        if length % size == 0:
            chunk = s[:size]
            if chunk * (length // size) == s:
                return True
    return False

if __name__ == "__main__":
    main()
