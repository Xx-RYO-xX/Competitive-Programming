import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import product
    
    n, k, x = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    
    ans = []
    for idx in product(range(n), repeat=k):
        ans.append(''.join(s[i] for i in idx))
        
    ans.sort()
    print(ans[x-1])
    


if __name__ == '__main__':
    main()
