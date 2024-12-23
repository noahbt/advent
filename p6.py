#!/Users/noahthomas/Code/advent/venv/bin/python
import numpy as np
import sys
sys.setrecursionlimit(1000000)

DIRECTIONS_MAP = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
FNAME = 'input6'
HEIGHT, WIDTH = 130, 130
# FNAME = 'input6-2'
# HEIGHT, WIDTH = 10, 10

def _main():
    # Read
    with open(FNAME, 'r') as fp:
        lines = fp.readlines()
    
    # Create map and solve
    labmap, row, col, dir = create_labmap(lines)
    visited = []
    moves = count_moves(labmap, row, col, dir, moves=1, visited=visited)

    # Write
    with open('output6', 'w') as fp:
        np.savetxt(fp, labmap, fmt='%d', delimiter='')
    
    # Check solution
    mapcount = np.count_nonzero(labmap==2)
    unique_visited = set([(a, b) for (a, b, c) in visited])
    assert moves == mapcount == len(unique_visited)

    # Output result
    print(f'Part 1: Total distinct positions: {moves}')

    # loops = count_loops(labmap, visited)
    loops = count_loops_2(labmap, row, col, dir)
    print(f'Part 2: Total obstacle positions: {len(loops)}')


def create_labmap(lines):
    """
    Read lines and create map with 0 for open spots, and 1 for obstacles
    . = 0,  # = 1,  X = 2
    """
    labmap = np.zeros((HEIGHT, WIDTH), np.int8)
    for r, line in enumerate(lines):
        for c, l in enumerate(line.strip()):
            if l == '#':
                labmap[r][c] = 1
            elif l != '.':
                row, col, dir = r, c, DIRECTIONS_MAP[lines[r][c]]
    return labmap, row, col, dir


def count_moves(labmap, row, col, dir, moves, visited):
    """
    Recursively move one step at a time based on the next location based on the following possibilities
    1. Edge - we are done, return the number of unique positions
    2. Obstacle (#) - turn 90 degrees but don't increment unique position count
    3. Overlapping path (X) - make the move but don't increment unique position count
    4. Open spot (.) - make the move and increment unique position count
    """
    next_row = row + dir[0]
    next_col = col + dir[1]

    visited.append((row, col, dir))

    if next_row < 0 or next_row > HEIGHT - 1 or next_col < 0 or next_col > WIDTH - 1:
        labmap[row][col] = 2
        return moves
    elif labmap[next_row][next_col] == 1:
        dir = (dir[1], -dir[0])
        return count_moves(labmap, row, col, dir, moves, visited)
    elif labmap[next_row][next_col] == 2:
        labmap[row][col] = 2
        return count_moves(labmap, next_row, next_col, dir, moves, visited)
    else:
        labmap[row][col] = 2
        return count_moves(labmap, next_row, next_col, dir, moves + 1, visited)

def count_loops(labmap, visited):
    """
    Iterate through all moves and for each location
    - Place an obstacle immediately in front of the guard
    - Check if this creates a loop
    - If so, increase loops by 1
    """
    loops = []
    for i, (row, col, dir) in enumerate(visited):
        next_row = row + dir[0]
        next_col = col + dir[1]
        x = labmap[next_row][next_col]
        labmap[next_row][next_col] = 1
        newdir = (dir[1], -dir[0])
        if is_loop(labmap, row, col, newdir, []):
            print(f'Loop: {i+1:4d}/{len(visited)} - ({row:3d}, {col:3d}) - True')
            if (row, col) not in loops:
                loops.append((row, col))
        else:
            print(f'Loop: {i+1:4d}/{len(visited)} - ({row:3d}, {col:3d})')
        labmap[next_row][next_col] = x
    return loops
    # 1897 without duplicates
    # 1967 with duplicate locations
    # this means 108 false positives


def count_loops_2(labmap, row, col, dir):
    """
    Given the map and a starting row, col, check if you loop
    """
    loops = []
    for r in range(130):
        for c in range(130):
            i = r * 130 + c
            x = labmap[r][c]
            labmap[r][c] = 1
            if is_loop(labmap, row, col, dir, []):
                print(f'Loop: {i+1:4d}/{130*130} - ({r:3d}, {c:3d}) - True')
                loops.append((r, c))
            else:
                print(f'Loop: {i+1:4d}/{130*130} - ({r:3d}, {c:3d})')
            labmap[r][c] = x
    return loops


def is_loop(labmap, row, col, dir, curr_visited):
    """
    Recursively trace the guard's path until
    - The next position is an edge, return False
    - The next position has been seen before
      - If this is the case, this is a loop
      - Return True
    """
    next_row = row + dir[0]
    next_col = col + dir[1]

    if next_row < 0 or next_row > HEIGHT - 1 or next_col < 0 or next_col > WIDTH - 1:
       # edge - can't put obstacle
        return False
    elif labmap[next_row][next_col] == 1:
        # obstacle - don't check
        dir = (dir[1], -dir[0])
        return is_loop(labmap, row, col, dir, curr_visited)
    else:
        # open spot or visited
        if (row, col, dir) in curr_visited:
            return True
        curr_visited.append((row, col, dir))
        return is_loop(labmap, next_row, next_col, dir, curr_visited)


if __name__ == '__main__':
    _main()
