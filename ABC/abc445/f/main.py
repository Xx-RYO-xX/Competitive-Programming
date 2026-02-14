import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    c = [0]
    for _ in range(n):
        ct = [0] + list(map(int, input().split()))
        c.append(ct)


if __name__ == "__main__":
    main()
