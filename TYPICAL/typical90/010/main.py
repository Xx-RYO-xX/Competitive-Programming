import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate
    n = int(input())
    one = []
    two = []
    for _ in range(n):
        c, p = map(int, input().split())
        if c == 1:
            one.append(p)
            two.append(0)
        else:
            one.append(0)
            two.append(p)
    one = [0] + list(accumulate(one))
    two = [0] + list(accumulate(two))
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        a = one[r] - one[l-1]
        b = two[r] - two[l-1]
        print(a, b)


if __name__ == '__main__':
    sys.exit(main())
