import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    def calc(k):
        return (k*(k+1))//2

    left = 1
    right = n
    
    while left < right:
        mid = (left + right+1)//2
        if calc(mid) <= n+1:
            left = mid
        else:
            right = mid-1

    print(1+n-left)

if __name__ == '__main__':
    main()
