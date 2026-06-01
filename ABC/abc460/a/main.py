import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())

    ans = 0
    while m != 0:
        m = n % m
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
