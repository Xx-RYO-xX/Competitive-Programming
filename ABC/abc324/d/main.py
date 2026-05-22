import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    from math import sqrt

    n = int(input())
    s = input()

    ss = Counter(s)
    ans = 0
    for i in range(int(sqrt(10**n)) + 2):
        num = Counter(str(i**2).zfill(n))
        ans += num == ss

    print(ans)


if __name__ == "__main__":
    main()
