import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        c, s, z = map(int, input().split())
        x.append(c - 1)
        y.append(s - z)
    for i in range(n - 1):
        if not ((x[i] == x[i + 1] and y[i] < y[i + 1]) or x[i] > x[i + 1]):
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
