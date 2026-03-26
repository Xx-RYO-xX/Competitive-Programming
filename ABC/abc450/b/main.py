import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    cost = dict()
    for i in range(1, n):
        cc = list(map(int, input().split()))
        for j, ccc in zip(range(i + 1, n + 1), cc):
            cost[(i, j)] = ccc

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if cost[(a, c)] > cost[(a, b)] + cost[(b, c)]:
                    print("Yes")
                    return

    print("No")


if __name__ == "__main__":
    main()
