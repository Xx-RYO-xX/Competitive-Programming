import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, r, t = map(int, input().split())
    p = list(map(int, input().split()))

    for P in p:
        print(min(r, t // P), end=" ")


if __name__ == "__main__":
    main()
