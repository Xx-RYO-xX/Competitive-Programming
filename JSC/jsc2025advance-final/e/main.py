import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from random import randrange

    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))

    for _ in range(100):
        i = randrange(n)
        j = i
        while j == i:
            j = randrange(n)

        x1, y1 = xy[i]
        x2, y2 = xy[j]
        cnt = 2
        for k in range(n):
            if k != i and k != j:
                x3, y3 = xy[k]
                if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                    cnt += 1

        if cnt * 2 >= n:

            a = y2 - y1
            b = x1 - x2
            c = x2 * y1 - x1 * y2

            print("Yes")

            print(a, b, c)
            return

    print("No")


if __name__ == "__main__":
    main()
