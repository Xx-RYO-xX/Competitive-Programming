import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    t = list(map(int, input().split()))

    for i in range(n):
        t[i] = (t[i], i + 1)

    t.sort()
    print(*[t[i][1] for i in range(3)])


if __name__ == "__main__":
    main()
