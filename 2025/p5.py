#!/usr/bin/env python3

TEST_INPUT = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32"
]

def main():
    with open('input5.txt', 'r') as f:
        data = f.readlines()
    # data = TEST_INPUT
    # fresh_ingredients = get_fresh_ingredients(data)
    # print(f"Number of fresh ingredients: {len(fresh_ingredients)}")
    num_range_ingredients = count_range_ingredients(data)
    print(f"Number of ingredients in ranges: {num_range_ingredients}")

def get_fresh_ingredients(data):
    i = 0
    fresh_ranges = []
    while i < len(data):
        line = data[i].strip()
        if line == "":
            i += 1
            break
        parts = line.split('-')
        start = int(parts[0])
        end = int(parts[1])
        fresh_ranges.append((start, end))
        i += 1

    fresh_ingredients = []
    while i < len(data):
        line = data[i].strip()
        ingredient = int(line)
        is_fresh = False
        for fr in fresh_ranges:
            if fr[0] <= ingredient <= fr[1]:
                is_fresh = True
                break
        if is_fresh:
            fresh_ingredients.append(ingredient)
        i += 1

    return fresh_ingredients

def count_range_ingredients(data):
    # Get all ranges, then merge any overlapping ranges
    ranges = []
    for line in data:
        line = line.strip()
        if line == "":
            break
        parts = line.split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))

    if not ranges:
        return 0

    # sort them by the start value
    ranges.sort()
    merged = []
    cur_start, cur_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))

    # count total ingredients in merged ranges
    ingredient_count = sum(end - start + 1 for start, end in merged)
    return ingredient_count

if __name__ == "__main__":
    main()
