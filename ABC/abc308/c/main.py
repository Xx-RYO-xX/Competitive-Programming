import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from decimal import Decimal, getcontext
    n = int(input())
    
    getcontext().prec = 100
    def seikou(a, b):
        return a/(a+b)
    
    ans = defaultdict(list)
    for i in range(1, n+1):
        a, b = map(Decimal, input().split())
        ans[seikou(a, b)].append(i)
    
    for a in sorted(ans, reverse=True):
        print(*ans[a], sep="\n")

if __name__ == '__main__':
    sys.exit(main())
