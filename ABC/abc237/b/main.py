import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import numpy as np

    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split()))[::-1])
    a = np.array(a)
    a = np.rot90(a)

    for A in a:
        print(*A)


if __name__ == "__main__":
    main()
