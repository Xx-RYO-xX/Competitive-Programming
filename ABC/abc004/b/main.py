import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import numpy as np
    c = []
    for _ in range(4):
        c.append(list(input().split()))

    c = np.array(c)

    c = np.rot90(c, 2)
    
    for row in c:
        print(' '.join(row))


if __name__ == '__main__':
    main()
