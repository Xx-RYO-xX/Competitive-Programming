import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3

    print("Yes" if n == 1 else "No")


if __name__ == "__main__":
    main()
