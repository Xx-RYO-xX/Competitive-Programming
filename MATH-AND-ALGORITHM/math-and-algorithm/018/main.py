import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(a.count(100) * a.count(400) + a.count(200) * a.count(300))


if __name__ == "__main__":
    main()
