import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from fractions import Fraction

    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]

                if (x1 == x2 == x3) or (y1 == y2 == y3):
                    print("Yes")
                    return
                else:
                    try:
                        a = Fraction(y2 - y1, x2 - x1)
                    except:
                        continue
                    b = y1 - x1 * a
                    if y3 == a * x3 + b:
                        print("Yes")
                        return

    print("No")


if __name__ == "__main__":
    main()
