import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import combinations
    from math import prod
    n, p, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    a_comb = combinations(a, 5)
    # print(a_comb)
    ans = 0
    for A, B, C, D, E in a_comb:
        if A%p * B%p * C%p * D%p * E%p  == q:
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
