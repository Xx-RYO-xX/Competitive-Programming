import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from decimal import Decimal
    from math import sqrt
    n, d = map(int, input().split())
    zahyou = []
    for _ in range(n):
        zahyou.append(list(map(int, input().split())))
    
    def calc(lst1, lst2):
        ans = 0
        for i in range(d):
            ans += (lst1[i] - lst2[i])**2
        return sqrt(ans)

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if calc(zahyou[i], zahyou[j]).is_integer():
                ans += 1
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
