import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, m, x = map(int, input().split())

    for _ in range(m):
        u, v = map(int, input().split())



if __name__ == '__main__':
    sys.exit(main())
