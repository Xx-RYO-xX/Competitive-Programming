import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    cnt = 0
    for _ in range(n):
        s = input()
        if s == "For":
            cnt += 1

    print("Yes" if n // 2 < cnt else "No")


if __name__ == "__main__":
    main()
