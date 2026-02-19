import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    h = list(map(int, input().split()))

    ans = 1
    m = h[0]
    for i in range(1, n):
        if h[i] > m:
            ans += 1
            m = h[i]

    print(ans)


if __name__ == "__main__":
    main()
