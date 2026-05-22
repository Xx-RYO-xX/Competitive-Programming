import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    print("Yes" if all([a[i] == a[0] for i in range(n)]) else "No")


if __name__ == "__main__":
    main()
