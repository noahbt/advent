#!/Users/noahthomas/Code/advent/venv/bin/python
import numpy as np

FNAME = 'input8'

def _main():
    # Read
    with open(FNAME, 'r') as fp:
        diskmap = fp.read()
    
    filemap = create_filemap(diskmap)

    compacted = compact_filemap(filemap)

    checksum = compute_checksum(compacted)

    # Output result
    print(f'Part 1: Computed checksum: {checksum}')


def create_filemap(diskmap):
    """
    Convert from 12345 to 0..111....22222
    """
    filemap = ''
    id = 0
    for i, c in enumerate(diskmap):
        if i % 2 == 0:
            filemap += f'{id}' * int(c)
            id += 1
        else:
            filemap += '.' * int(c)
    return filemap


def compact_filemap(filemap):
    """
    Compact the filemap
    0..111....22222
    022111222
    """
    i = 0
    j = len(filemap) - 1
    result = ''
    while i < j:
        if filemap[i] != '.':
            result += filemap[i]
            i += 1
        else:
            if filemap[j] != '.':
                result += filemap[j]
                i += 1
            j -= 1
    return result
    

def compute_checksum(compacted):
    """
    0938288002
    0*0 + 1*9 + 2*3 + 3*8 ...
    """
    checksum = 0
    for i, c in enumerate(compacted):
        checksum += i * int(c)
    return checksum



if __name__ == '__main__':
    _main()
