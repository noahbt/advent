#!/Users/noahthomas/Code/advent/venv/bin/python
import numpy as np

FNAME = 'input8'
HEIGHT, WIDTH = 50, 50
# FNAME = 'input8-2'
# HEIGHT, WIDTH = 12, 12

def _main():
    # Read
    with open(FNAME, 'r') as fp:
        lines = fp.readlines()
    # map
    citymap = create_citymap(lines)
    # solve
    antinodes = set(find_antinodes(citymap))
    # Output result
    print(f'Part 1: Total unique antinodes: {len(antinodes)}')


def create_citymap(lines):
    """
    Create citymap with the type, and location of every antenna
    """
    citymap = {}
    for r, line in enumerate(lines):
        for c, l in enumerate(line.strip()):
            if l != '.':
                if l not in citymap:
                    citymap[l] = []
                citymap[l].append((r, c))
    return citymap


def find_antinodes(citymap):
    """
    For every pair on the map, calculate their antinodes
    """
    antinodes = []
    for k in citymap.keys():
        antenna_coords = citymap[k]
        antenna_pairs = get_pairs(antenna_coords)
        for pair in antenna_pairs:
            # antinodes.extend(get_antinodes(pair))
            antinodes.extend(get_antinodes_2(pair))
    return antinodes


def get_pairs(coords):
    return [(a, b) for idx, a in enumerate(coords) for b in coords[idx + 1:]]


def get_antinodes(pair):
    a, b = pair
    diff = (b[0] - a[0], b[1] - a[1])
    coords = [(a[0] - diff[0], a[1] - diff[1]), (b[0] + diff[0], b[1] + diff[1])]
    antinodes = []
    for coord in coords:
        if in_map(coord):
            antinodes.append(coord)
    return antinodes


def get_antinodes_2(pair):
    a, b = pair
    diff = (b[0] - a[0], b[1] - a[1])
    r, c = (a[0], a[1])
    antinodes = []
    while in_map((r, c)):
        antinodes.append((r, c))
        r -= diff[0]
        c -= diff[1]
    r,c = (b[0], b[1])
    while in_map((r, c)):
        antinodes.append((r, c))
        r += diff[0]
        c += diff[1]
    return antinodes


def in_map(node):
    return node[0] >= 0 and node[0] < WIDTH and node[1] >= 0 and node[1] < HEIGHT


if __name__ == '__main__':
    _main()
