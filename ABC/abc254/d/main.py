import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from math import sqrt

    n = int(input())

    # f(x) = k**2 * d (k**2はxを割り切る最大のk**2)
    # f(i)*f(j)が平方数になるには、d == d にならなければならない

    dcnt = defaultdict(int)
    i_to_d = dict()
    for i in range(1, n + 1):
        for k in range(1, int(sqrt(i)) + 1)[::-1]:
            if i % k**2 == 0:
                d = i // k**2
                dcnt[d] += 1
                i_to_d[i] = d
                break

    ans = 0
    for i in range(1, n + 1):
        ans += dcnt[i_to_d[i]]

    print(ans)


if __name__ == "__main__":
    main()
