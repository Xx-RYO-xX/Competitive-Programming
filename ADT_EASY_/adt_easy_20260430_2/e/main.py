import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from time import time

    n, x, y = map(int, input().split())

    red = defaultdict(int)
    blue = defaultdict(int)

    red[n] = 1
    start = time()

    while any([red[i] > 0 for i in range(2, n + 1)]) or any(
        [blue[i] > 0 for i in range(2, n + 1)]
    ):
        if time() - start > 1.9:
            print(0)
            return
        for nn in range(2, n + 1)[::-1]:
            # print(nn)
            if red[nn] > 0:
                red[nn - 1] += red[nn]
                blue[nn] += x * red[nn]
                red[nn] = 0
            if blue[nn] > 0:
                red[nn - 1] += blue[nn]
                blue[nn - 1] += y * blue[nn]
                blue[nn] = 0

    print(blue[1])


if __name__ == "__main__":
    main()
