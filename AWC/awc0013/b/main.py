import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    friend = set()
    ans = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if (b, a) in friend:
            ans += 1
        else:
            friend.add((a, b))

    print(ans)


if __name__ == "__main__":
    main()
