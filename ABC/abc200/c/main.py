def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        a[i] %= 200
    
    from collections import Counter
    cnt = Counter(a)

    from math import comb 
    ans = 0
    for c in cnt:
        if cnt[c] > 1:
            ans += comb(cnt[c], 2)
    print(ans)
    
if __name__ == "__main__":
    main()
