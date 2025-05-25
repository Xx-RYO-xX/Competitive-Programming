import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import math
    from collections import Counter
    n = int(input())
    a = [int(input()) for _ in range(n)]

    ans = 0
    cnt = Counter(a)
    for c in cnt:
        ans += math.comb(cnt[c], 2)
    
    print(ans)

if __name__ == '__main__':
    main()
