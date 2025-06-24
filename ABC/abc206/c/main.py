import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    a = list(set(a))
    
    ans = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            ans += cnt[a[i]]*cnt[a[j]]
    
    print(ans)

if __name__ == '__main__':
    main()
