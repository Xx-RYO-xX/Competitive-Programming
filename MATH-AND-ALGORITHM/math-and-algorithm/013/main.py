import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import math

    n = int(input())

    ans = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)

    for an in sorted(ans):
        print(an)


if __name__ == "__main__":
    main()
