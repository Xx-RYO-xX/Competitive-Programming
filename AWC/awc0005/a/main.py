import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for aa in a:
        if aa % k == 0:
            ans += aa

    print(ans)


if __name__ == "__main__":
    main()
