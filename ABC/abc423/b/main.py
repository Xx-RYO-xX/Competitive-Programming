import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    l = list(map(int, input().split()))

    b1, a1 = None, None

    for i in range(n):
        if b1 == None and l[i] == 1:
            b1 = i
        if a1 == None and l[-1 - i] == 1:
            a1 = n - 1 - i

    if b1 == a1:
        print(0)
    else:
        print(a1 - b1)


if __name__ == "__main__":
    main()
