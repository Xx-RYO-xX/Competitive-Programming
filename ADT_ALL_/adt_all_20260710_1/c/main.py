import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    x, y = map(int, input().split())
    print(a[x - 1][y])


if __name__ == "__main__":
    main()
