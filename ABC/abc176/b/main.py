import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = list(input())
    ans = 0
    for N in n:
        ans += int(N)
    print("Yes" if ans % 9 == 0 else "No")


if __name__ == "__main__":
    main()
