import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b, c = map(int, input().split())
    ans = c * (b - a)
    print(ans if ans >= 0 else 0)


if __name__ == "__main__":
    main()
