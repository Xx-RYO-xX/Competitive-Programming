import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, p = map(int, input().split())
    print((3 * a + p) // 2)


if __name__ == "__main__":
    main()
