import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import product

    n, k = map(int, input().split())

    t = []
    for _ in range(n):
        t.append(list(map(int, input().split())))

    for prod in product(*t):
        tt = prod[0]
        for i in range(1, n):
            tt ^= prod[i]
        if tt == 0:
            print("Found")
            return
    print("Nothing")


if __name__ == "__main__":
    main()
