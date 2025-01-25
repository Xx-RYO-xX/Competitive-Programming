import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))
    
    def mid_check(x):
        count = 0
        slice_len = 0
        for i in range(n):
            if x <= a[i] - slice_len:
                count += 1
                slice_len = a[i]
        
        if x <= l - slice_len:
            count += 1
        
        return  k+1 <= count
    
    
    left = 0
    right = l+1
    while right - left > 1:
        mid = (left+right)//2
        
        if mid_check(mid):
            left = mid
        else:
            right = mid
    
    print(left)


if __name__ == '__main__':
    sys.exit(main())
