import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import combinations

    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for comb in combinations(a, 5):
        ans += sum(comb) == 1000

    print(ans)


if __name__ == "__main__":
    main()
