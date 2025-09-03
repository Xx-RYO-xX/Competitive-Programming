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
            for k in range(j + 1, n):
                x3, y3 = xy[k]
                if (y1 - y2) * (x2 - x3) != (x1 - x2) * (y2 - y3):
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
