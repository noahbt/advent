#!/usr/bin/env python3

TEST_INPUT = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@."
]

def main():
    with open('input4.txt', 'r') as f:
        data = f.readlines()
    # data = TEST_INPUT
    for i in range(len(data)):
        data[i] = list(data[i].strip())
    roll_locations = get_location_count(data)
    print(f"Number of roll locations: {roll_locations}")

def get_location_count(data):
    # continuously try to find roll locations until no more can be found
    locations = get_roll_locations(data)
    count = len(locations)
    total_locations = count
    for loc in locations:
        row, col = loc
        data[row][col] = '.'
    depth = 0

    while count > 0 and depth < 100:
        locations = get_roll_locations(data)
        count = len(locations)
        total_locations += count
        for loc in locations:
            row, col = loc
            data[row][col] = '.'
        depth += 1

    print(depth)
    return total_locations

def get_roll_locations(data):
    locations = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '@':
                # Check surrounding cells for '@'
                cells = get_surrounding_cells(data, row, col)
                count_at = sum(1 for r, c, val in cells if val == '@')
                if count_at < 4:
                    locations.append((row, col))
    return locations

def get_surrounding_cells(data, row, col):
    cells = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(data) and 0 <= c < len(data[r]):
            cells.append((r, c, data[r][c]))
    return cells

if __name__ == "__main__":
    main()
