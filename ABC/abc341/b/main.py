import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    for i in range(1, n):
        s, t = map(int, input().split())
        a[i + 1] += t * (a[i] // s)

    print(a[n])


if __name__ == "__main__":
    main()
