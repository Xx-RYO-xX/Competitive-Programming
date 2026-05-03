import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, a, b = map(int, input().split())
    ans = 0
    cnt = 5
    for i in range(n):
        if cnt > 0:
            ans += b
            cnt -= 1
        else:
            ans += a
    print(ans)


if __name__ == "__main__":
    main()
