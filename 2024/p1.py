#!/usr/bin/python3

def _main():
    lines = []
    with open('input1', 'r') as fp:
        lines = fp.readlines()
    
    left = []
    right = []
    for line in lines:
        delim = '   '
        a, b = line.strip().split(delim)
        left.append(int(a))
        right.append(int(b))
    
    left.sort()
    right.sort()

    dist = 0
    for i in range(len(left)):
        dist += abs(left[i] - right[i])
    
    print(dist)

    # convert to int then sort and calculate


if __name__ == '__main__':
    _main()
