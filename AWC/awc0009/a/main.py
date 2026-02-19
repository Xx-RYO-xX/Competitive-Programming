import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    k, m = map(int, input().split())
    l = list(map(int, input().split()))

    print(sum(l) % m)


if __name__ == "__main__":
    main()
