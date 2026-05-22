import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, x = map(int, input().split())
    kanzou = 0
    for i in range(n):
        v, p = map(int, input().split())
        kanzou += v * p
        if kanzou > x * 100:
            print(i + 1)
            return
    print(-1)


if __name__ == "__main__":
    main()
