import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    anst = sum(a)
    for i in range(n):
        if anst - a[i] == m:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
