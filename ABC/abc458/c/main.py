import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == "C":
            ans += min(i, n - 1 - i) + 1

    print(ans)


if __name__ == "__main__":
    main()
