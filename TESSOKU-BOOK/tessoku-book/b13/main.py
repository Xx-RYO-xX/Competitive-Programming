import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a = list(accumulate(a, initial=0))
    # print(a)
    ans = 0

    for i in range(1, n+1):
        left, right = i, n+1
        while left < right:
            mid_idx = (left+right)//2
            mid_yen = a[mid_idx] - a[i-1]

            if mid_yen <= k:
                left = mid_idx+1
            else:
                right = mid_idx
        # print(i, left, right)
        ans += left-i
    
    print(ans)

if __name__ == '__main__':
    main()
