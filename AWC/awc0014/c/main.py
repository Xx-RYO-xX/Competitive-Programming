import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    g, m, d, k, v = map(int, input().split())
    if g - (d * k) > 0:
        print("Yes" if v * (k + (g - (d * k))) <= (m - g) / v else "No")
    else:
        print("Yes" if g / d <= (m - g) / v else "No")


if __name__ == "__main__":
    main()
