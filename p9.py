#!/Users/noahthomas/Code/advent/venv/bin/python
import numpy as np

FNAME = 'input9'
# FNAME = 'input9-2'

def _main():
    # Read
    with open(FNAME, 'r') as fp:
        diskmap = fp.read()
    
    filemap = create_filemap(diskmap)
    print(f'Filemap: {filemap}')

    compacted = compact_filemap(filemap)
    print(f'Compacted: {compacted}')

    checksum = compute_checksum(compacted)

    # Output result
    print(f'Part 1: Computed checksum: {checksum}')


def create_filemap(diskmap):
    filemap = []
    id = 0
    for i, c in enumerate(diskmap):
        if i % 2 == 0:
            filemap.extend([id] * int(c))
            id += 1
        else:
            filemap.extend([-1] * int(c))
    return filemap


def compact_filemap(filemap):
    i = 0
    j = len(filemap) - 1
    result = []
    while i <= j:
        if filemap[i] >= 0:
            result.append(filemap[i])
            i += 1
        else:
            if filemap[j] >= 0:
                result.append(filemap[j])
                i += 1
            j -= 1
    while i < len(filemap):
        result.append(-1)
        i += 1
    return result


def compute_checksum(compacted):
    checksum = 0
    for i, x in enumerate(compacted):
        if x >= 0:
            checksum += i * x
    return checksum


if __name__ == '__main__':
    _main()

# 89312744865 was not right
# 6283170117911 after using int arrays