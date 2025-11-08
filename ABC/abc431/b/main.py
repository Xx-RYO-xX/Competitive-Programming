import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x = int(input())
    n = int(input())
    w = list(map(int, input().split()))
    q = int(input())
    connect = set()
    for _ in range(q):
        p = int(input()) - 1
        if p in connect:
            x -= w[p]
            connect.discard(p)
        else:
            x += w[p]
            connect.add(p)
        print(x)


if __name__ == "__main__":
    main()
