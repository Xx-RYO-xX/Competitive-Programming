import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    xy = defaultdict(list)
    for _ in range(3):
        x, y = map(int, input().split())
        xy[x].append(y)

    xs = []
    for xxyy in xy:
        xs.append(xxyy)
    x1, x2 = xs[0], xs[1]
    if len(xy[x1]) > len(xy[x2]):
        x1, x2 = x2, x1

    xy[x2].remove(xy[x1][0])
    print(x1, *xy[x2])


if __name__ == "__main__":
    main()
