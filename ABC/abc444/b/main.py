import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        if sum(map(int, str(i))) == k:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
