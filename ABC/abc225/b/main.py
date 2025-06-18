import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    
    n = int(input())
    star = defaultdict(set)
    for _ in range(n-1):
        a, b = map(int, input().split())
        star[a].add(b)
        star[b].add(a)
    
    for i in range(1, n+1):
        if len(star[i]) == n-1:
            print("Yes")
            return
    
    print("No")
    
    


if __name__ == '__main__':
    main()
