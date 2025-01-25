import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import math
    r = int(input())
    
    ans = 0
    for x in range(r+1):
        if (x + 0.5)**2 + 0.5**2 > r**2:
            break
        left, right = 0, r+1
        while left < right:
            mid = (left + right + 1) // 2
            if (x + 0.5)**2 + (mid + 0.5)**2 <= r**2:
                left = mid
            else:
                right = mid - 1
        if x == 0:
            ans += 1 + left * 2
        else:
            ans += 2 + left * 4
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
