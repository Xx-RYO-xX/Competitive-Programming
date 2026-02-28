import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())

    print("Yes" if (n + 1) // 2 >= m else "No")


if __name__ == "__main__":
    main()
