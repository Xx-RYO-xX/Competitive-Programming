import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    xy.sort()

    ans = 0
    miny = float("inf")
    for x, y in xy:
        if y < miny:
            ans += 1
            miny = y

    print(ans)


if __name__ == "__main__":
    main()
