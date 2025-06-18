import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    from math import comb
    n = int(input())
    a = list(map(int, input().split()))
    
    a_cnt = Counter(a)
    ans = 0
    for AA in a_cnt:
        ans += comb(a_cnt[AA], 2)
    
    # print(a_cnt)
    # print(ans)
    # print()
    for k in range(n):
        print(ans-comb(a_cnt[a[k]], 2)+comb(a_cnt[a[k]]-1, 2))


if __name__ == '__main__':
    sys.exit(main())
