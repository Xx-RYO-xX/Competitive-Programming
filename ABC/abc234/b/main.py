import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))

    ans = 0
    for i in range(n):
        x1, y1 = xy[i]
        for j in range(i + 1, n):
            x2, y2 = xy[j]
            ans = max(ans, (x1 - x2) ** 2 + (y1 - y2) ** 2)

    print(ans ** (1 / 2))


if __name__ == "__main__":
    main()
