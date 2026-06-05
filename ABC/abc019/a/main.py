import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    abc = sorted(map(int, input().split()))
    print(abc[1])


if __name__ == "__main__":
    main()
