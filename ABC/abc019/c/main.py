import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from bisect import bisect_right

    n = int(input())
    a = sorted(map(int, input().split()))

    ans = set()

    for A in a:
        while A % 2 == 0:
            A //= 2
        ans.add(A)

    print(len(ans))


if __name__ == "__main__":
    main()
