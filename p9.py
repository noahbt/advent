#!/Users/noahthomas/Code/advent/venv/bin/python
import numpy as np

FNAME = 'input9'
# FNAME = 'input9-2'

def _main():
    # Read
    with open(FNAME, 'r') as fp:
        diskmap = fp.read()
    
    filemap = create_filemap(diskmap)
    # print(f'Filemap: {filemap}')

    compacted = compact_filemap(filemap)
    # print(f'Compacted: {compacted}')

    checksum = compute_checksum(compacted)

    # Output result
    print(f'Part 1: Computed checksum: {checksum}')

    # filemap2 = create_filemap_2(diskmap)
    filemap_2 = create_filemap_2(diskmap)
    compact_filemap_2(filemap_2)
    checksum_2 = compute_checksum(to_fragments(sorted(filemap_2)))

    # Output result
    print(f'Part 2: Computed checksum: {checksum_2}')


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


def create_filemap_2(diskmap):
    """
    2333133121414131402
    [
        (index 0, id 0, size 2)
        (index 2, id -1, size 3)
        (index 5, id 1, size 3)
        ...
    ]
    """
    filemap = []
    id, idx = 0, 0
    for i, c in enumerate(diskmap):
        if i % 2 == 0:
            # file
            size = int(c)
            filemap.append((idx, id, size))
            id += 1
            idx += size
        else:
            # space
            size = int(c)
            filemap.append((idx, -1, size))
            idx += size
    return filemap


def compact_filemap(filemap):
    i, j = 0, len(filemap) - 1
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

def compact_filemap_2(filemap):
    """
    Modify the filemap to take up space
    2333133121414131402
    [(index 0, id 0, size 2), (index 2, id -1, size 3), (index 5, id 1, size 3), ...]
    """
    j = len(filemap) - 1
    while j > 0:
        if filemap[j][1] == -1:
            j -= 1
            continue
        file_idx, file_id, file_size = filemap[j]
        i = 1
        # keep iterating if you're not on free space, or free space is too small
        while i < j and (filemap[i][1] != -1 or file_size > filemap[i][2]):
            i += 1
        if i < j:
            free_idx, _, free_size = filemap[i]
            leftover = free_size - file_size
            filemap[j] = (free_idx, file_id, file_size)
            filemap[i] = (free_idx + file_size, -1, leftover)
            filemap.append((file_idx, -1, file_size))
        j -= 1
    return filemap


def to_fragments(filemap):
    # from file array into fragment array
    result = []
    for _, id, size in filemap:
        if id == -1:
            result.extend([-1] * size)
        else:
            result.extend([id] * size)
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