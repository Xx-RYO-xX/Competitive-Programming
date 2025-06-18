import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m, q = map(int, input().split())

    for _ in range(m):
        a, b, c, d = map(int, input().split())


if __name__ == '__main__':
    sys.exit(main())
