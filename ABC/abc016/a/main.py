import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    m, d = map(int, input().split())

    print("YES" if m % d == 0 else "NO")


if __name__ == "__main__":
    main()
