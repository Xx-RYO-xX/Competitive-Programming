import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        a -= 1
        if c[a] >= b:
            ans += b
            c[a] -= b
        else:
            ans += c[a]
            c[a] = 0
    print(ans)


if __name__ == "__main__":
    main()
