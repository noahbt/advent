#!/Users/noahthomas/Code/advent/venv/bin/python
import numpy as np
import sys
sys.setrecursionlimit(10000)

DIRECTIONS_MAP = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
HEIGHT, WIDTH = 130, 130

def _main():
    # Read
    with open('input6', 'r') as fp:
        lines = fp.readlines()
    
    # Create map and solve
    labmap, row, col, dir = create_labmap(lines)
    obstacle_map = {dir: [] for dir in DIRECTIONS_MAP.values()}
    moves, positions = count_moves(labmap, row, col, dir, 1, obstacle_map, 0)

    # Write
    with open('output6', 'w') as fp:
        np.savetxt(fp, labmap, fmt='%d', delimiter='')
    
    # Check solution
    mapcount = np.count_nonzero(labmap==2)
    assert moves == mapcount

    # Output result
    print(f'Part 1: Total distinct positions: {moves}')
    print(f'Part 2: Total obstacle positions: {positions}')


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


def count_moves(labmap, row, col, dir, moves, obstacle_map, positions):
    """
    Recursively move one step at a time based on the next location based on the following possibilities
    1. Edge - we are done, return the number of unique positions
    2. Obstacle (#) - turn 90 degrees but don't increment unique position count
    3. Overlapping path (X) - make the move but don't increment unique position count
    4. Open spot (.) - make the move and increment unique position count
    """
    next_row = row + dir[0]
    next_col = col + dir[1]

    if next_row < 0 or next_row > HEIGHT - 1 or next_col < 0 or next_col > WIDTH - 1:
        labmap[row][col] = 2
        return moves, positions
    elif labmap[next_row][next_col] == 1:
        obstacle_map[dir].append((row, col))
        dir = (dir[1], -dir[0])
        return count_moves(labmap, row, col, dir, moves, obstacle_map, positions)
    elif labmap[next_row][next_col] == 2:
        next_dir = (dir[1], -dir[0])
        obstacles = obstacle_map[next_dir]
        for o in obstacles:
            obr = o[0]
            obc = o[1]
            if dir == (-1, 0) and obr == row and obc > col: # up
                positions += 1
            elif dir == (0, 1) and obr > row and obc == col: # right
                positions += 1
            elif dir == (1, 0) and obr == row and obc < col: # down
                positions += 1
            elif dir == (0, -1) and obr < row and obc == col: # left
                positions += 1
        labmap[row][col] = 2
        return count_moves(labmap, next_row, next_col, dir, moves, obstacle_map, positions)
    else:
        next_dir = (dir[1], -dir[0])
        obstacles = obstacle_map[next_dir]
        for o in obstacles:
            obr = o[0]
            obc = o[1]
            if dir == (-1, 0) and obr == row and obc > col: # up
                positions += 1
            elif dir == (0, 1) and obr > row and obc == col: # right
                positions += 1
            elif dir == (1, 0) and obr == row and obc < col: # down
                positions += 1
            elif dir == (0, -1) and obr < row and obc == col: # left
                positions += 1
        labmap[row][col] = 2
        return count_moves(labmap, next_row, next_col, dir, moves + 1, obstacle_map, positions)


if __name__ == '__main__':
    _main()


## Part 2
"""
r = current row
c = current col
TODO - might have to adjust obr < r - 1 or something

When moving left
- Place obstacle one left of top obstacles
- If there exists a previous obstacle that obr < r and obc == c

When moving right
- Place obstacle one right of bottom obstacles
- obr > r and obc == c

When moving up
- Place obstacle one up of right obstacles
- obr == r and obc > c

When moving down
- Place obstacle one down of left obstacles
- obr == r and obc < c

Top obstacles means you turn from up to right

So just keep track of previous obstacles and their type

"""