import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split()))[1:])
    x, y = map(lambda x: int(x) - 1, input().split())
    print(a[x][y])


if __name__ == "__main__":
    main()
