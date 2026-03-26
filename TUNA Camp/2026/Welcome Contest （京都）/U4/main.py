import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())

    for _ in range(q):
        a, b = map(int, input().split())


if __name__ == "__main__":
    main()
