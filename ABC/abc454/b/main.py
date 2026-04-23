import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    f = list(map(int, input().split()))

    print("Yes" if len(f) == len(set(f)) else "No")
    print("Yes" if len(set(f)) == m else "No")


if __name__ == "__main__":
    main()
