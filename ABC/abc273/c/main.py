import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    n = int(input())
    a = sorted(map(int, input().split()))
    print(a)
    a_cnt = Counter(a)
    accm = []
    for i in range(1, n+1):
        accm.append(n-(i+a_cnt[a[i-1]]-1))
        a_cnt[a[i-1]] -=1
    print(accm)

if __name__ == '__main__':
    sys.exit(main())
