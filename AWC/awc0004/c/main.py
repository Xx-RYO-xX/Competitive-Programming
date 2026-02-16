import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    h = list(map(int, input().split())) + [0]

    print(abs(max(h) - min(h)) * 2)


if __name__ == "__main__":
    main()
