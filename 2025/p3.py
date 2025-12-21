#!/usr/bin/env python

TEST_INPUT = """987654321111111
811111111111119
234234234234278
818181911112111"""

def main():
    # with open('input3', 'r') as f:
        # data = f.read()
    total_joltage = sum(get_max_joltage(TEST_INPUT))
    print(f"Total joltage: {total_joltage}")

def get_max_joltage(data):

if __name__ == "__main__":
    main()
