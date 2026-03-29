import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, f = map(int, input().split())
    if m == f == 1:
        print(n if n % 2 != 0 else n - 1)
        return
    if m == 1 and f == n:
        print(1)
        return


if __name__ == "__main__":
    main()
