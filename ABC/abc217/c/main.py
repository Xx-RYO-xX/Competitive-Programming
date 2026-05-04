import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    p = list(map(int, input().split()))

    q = []
    for i in range(n):
        q.append((p[i], i + 1))

    q.sort()
    print(*[q[i][1] for i in range(n)])


if __name__ == "__main__":
    sys.exit(main())
