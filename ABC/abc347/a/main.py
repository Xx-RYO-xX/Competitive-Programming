import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = map(int, input().split())

    for A in a:
        if A % k == 0:
            print(A // k, end=" ")


if __name__ == "__main__":
    main()
