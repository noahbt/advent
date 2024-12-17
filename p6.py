#!/Users/noahthomas/Code/advent/venv/bin/python
import numpy as np
import sys
sys.setrecursionlimit(10000)



def _main():
    # Read
    with open('input6', 'r') as fp:
        lines = fp.readlines()
    
    # Create map and solve
    labmap, row, col, dir = create_labmap(lines)
    obstacles = {(-1, 0): [], (0, 1): [], (1, 0): [], (0, -1): []}
    moves = count_moves(labmap, row, col, dir, 1, obstacles)

    # Write
    with open('output6', 'w') as fp:
        np.savetxt(fp, labmap, fmt='%d', delimiter='')
    
    # Check solution
    mapcount = np.count_nonzero(labmap==2)
    assert moves == mapcount

    # Output result
    print(f'Part 1: Total distinct positions: {moves}')


def create_labmap(lines):
    """
    Read lines and create map with 0 for open spots, and 1 for obstacles
    . = 0,  # = 1,  X = 2
    """
    labmap = np.zeros((130, 130), np.int8)
    dir_table = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    for r, line in enumerate(lines):
        for c, l in enumerate(line.strip()):
            if l == '#':
                labmap[r][c] = 1
            elif l != '.':
                row, col, dir = r, c, dir_table[lines[r][c]]
    return labmap, row, col, dir


def count_moves(labmap, row, col, dir, moves, obstacles):
    """
    Recursively move one step at a time based on the next location based on the following possibilities
    1. Edge - we are done, return the number of unique positions
    2. Obstacle (#) - turn 90 degrees but don't increment unique position count
    3. Overlapping path (X) - make the move but don't increment unique position count
    4. Open spot (.) - make the move and increment unique position count
    """
    r, c = dir
    next_row = row + r
    next_col = col + c

    if next_row < 0 or next_row > 129 or next_col < 0 or next_col > 129:
        labmap[row][col] = 2
        return moves
    elif labmap[next_row][next_col] == 1:
        obstacles[dir].append((row, col))
        dir = (dir[1], -dir[0])
        return count_moves(labmap, row, col, dir, moves, obstacles)
    elif labmap[next_row][next_col] == 2:
        # TODO check obstacle list
        labmap[row][col] = 2
        return count_moves(labmap, next_row, next_col, dir, moves, obstacles)
    else:
        # TODO check obstacle list
        labmap[row][col] = 2
        return count_moves(labmap, next_row, next_col, dir, moves + 1, obstacles)


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