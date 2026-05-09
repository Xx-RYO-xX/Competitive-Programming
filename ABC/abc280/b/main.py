import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = list(map(int, input().split()))

    a = [s[0]]
    for i in range(1, n):
        a.append(s[i] - sum(a))

    print(*a)


if __name__ == "__main__":
    main()
