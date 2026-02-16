import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    sa_ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        sa_ab.append((a - b, a, b))
    sa_ab.sort(reverse=True)

    ans = 0
    for i in range(n):
        sa, a, b = sa_ab[i]
        if 0 < k:
            ans += b
            k -= 1
        else:
            ans += a

    print(ans)


if __name__ == "__main__":
    main()
