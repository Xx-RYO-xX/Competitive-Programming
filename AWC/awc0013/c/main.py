import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    m, k = map(int, input().split())
    s = list(map(int, input().split()))

    print(sum([S < s[k - 1] for S in s]))


if __name__ == "__main__":
    main()
