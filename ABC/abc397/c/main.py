import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    left = set()
    left_count = {}  
    
    right = set()
    right_count = {}  
    
    left.add(a[0])
    left_count[a[0]] = 1
    
    for i in range(1, n):
        if a[i] not in right_count:
            right_count[a[i]] = 0
            right.add(a[i])
        right_count[a[i]] += 1
    
    ans = len(left) + len(right)
    
    for i in range(1, n):
        if a[i] not in left_count:
            left_count[a[i]] = 0
            left.add(a[i])
        left_count[a[i]] += 1
        
        right_count[a[i]] -= 1
        if right_count[a[i]] == 0:
            right.remove(a[i])
        
        anst = len(left) + len(right)
        ans = max(ans, anst)
    
    print(ans)

if __name__ == '__main__':
    sys.exit(main())