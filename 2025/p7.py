#!/usr/bin/env python3

TEST_INPUT = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "..............."
]

def main():
    with open('input7.txt', 'r') as f:
        data = f.readlines()
    # data = TEST_INPUT
    for i in range(len(data)):
        data[i] = list(data[i].strip())
    num_splits = count_splits(data)
    num_paths = count_paths(data)
    print(f"Total number of splits: {num_splits}")
    print(f"Number of paths from S to bottom: {num_paths}")

def count_splits(data):
    # given the grid, start from S and draw the path downwards
    # each time the path encounters a '^', it splits into two paths
    # count the number of splits and return that number
    num_splits = 0
    row = 0
    while row < len(data):
        col = 0
        while col < len(data[row]):
            c = data[row][col]
            if c == 'S':
                data[row + 1][col] = '|'
            elif c == '|':
                data[row + 1][col] = '|'
            elif c == '^' and data[row - 1][col] == '|':
                data[row][col - 1] = '|'
                data[row][col + 1] = '|'
                data[row + 1][col - 1] = '|'
                data[row + 1][col + 1] = '|'
                num_splits += 1
            elif row > 0 and data[row - 1][col] == '|':
                data[row + 1][col] = '|'
            col += 1
        row += 2
    return num_splits

def count_paths(grid):
    rows, cols = len(grid), len(grid[0])
    # Find the start position
    for c in range(cols):
        if grid[0][c] == 'S':
            start_col = c
            break

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(row, col):
        if not (0 <= col < cols):
            return 0
        if row == rows - 1:
            return 1
        cell = grid[row + 1][col]
        if cell == '^':
            left = dp(row + 1, col - 1) if col > 0 else 0
            right = dp(row + 1, col + 1) if col < cols - 1 else 0
            return left + right
        else:
            return dp(row + 1, col)

    return dp(0, start_col)

if __name__ == "__main__":
    main()
