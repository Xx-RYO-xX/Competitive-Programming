import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        if i <= m:
            print("OK")
        else:
            print("Too Many Requests")


if __name__ == "__main__":
    main()
