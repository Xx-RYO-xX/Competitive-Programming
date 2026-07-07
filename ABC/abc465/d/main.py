import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import floor

    for _ in range(int(input())):
        x, y, k = map(int, input().split())
        if x == y:
            print(0)
            continue

        lca = {x}
        xlca = {x: 0}
        dist = 0
        while x != 0:
            x = x // k
            lca.add(x)
            dist += 1
            xlca[x] = dist

        ylca = {y: 0}
        dist = 0
        while y not in lca:
            y = y // k
            dist += 1
            ylca[y] = dist
        print(xlca[y] + ylca[y])


if __name__ == "__main__":
    main()
