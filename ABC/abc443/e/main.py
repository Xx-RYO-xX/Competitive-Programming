import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    for _ in range(int(input())):
        n, c = map(int, input().split())
        s = []
        for i in range(n):
            s.append(input())


if __name__ == "__main__":
    main()
