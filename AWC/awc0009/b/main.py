import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, s, c = map(int, input().split())
    ans = 0
    for _ in range(n):
        h, p = map(int, input().split())
        if s >= h:
            s += -h + p
        else:
            ans += c

    print(ans)


if __name__ == "__main__":
    main()
