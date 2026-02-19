import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    e = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ei = min(e)

    print(sum([ei * cc for cc in c]))


if __name__ == "__main__":
    main()
