import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        aa = a[:]
        aa.pop(i)
        if sum(aa) == m:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
