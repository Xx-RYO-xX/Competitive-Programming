import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    p, q = map(int, input().split())
    x, y = map(int, input().split())
    print("Yes" if p <= x < p + 100 and q <= y < q + 100 else "No")


if __name__ == "__main__":
    main()
