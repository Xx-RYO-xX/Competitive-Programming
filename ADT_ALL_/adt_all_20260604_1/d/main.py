import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    xy = []
    for i in range(1, n + 1):
        x, y = map(int, input().split())
        xy.append((x, y, i))
    for i in range(n):
        x1, y1, num = xy[i]
        ans = None
        maxs = 0
        for j in range(n):
            x2, y2, anst = xy[j]
            lens = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if maxs < lens:
                maxs = lens
                ans = anst
        print(ans)


if __name__ == "__main__":
    main()
