import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = list(input())
    ans = 0
    for i in range(n - 2):
        if s[i] == s[i + 2] == "#" and s[i + 1] == ".":
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
