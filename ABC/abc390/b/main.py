import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    # from decimal import Decimal, getcontext
    # getcontext().prec = 100000
    
    n = int(input())
    a = list(map(int, input().split()))
    
    if n < 3:
        print("Yes")
        return
        
    
    gosa = 1e-9
    r = a[1] / a[0]
    for i in range(1, n):
        if abs(a[i - 1] * r - a[i]) > gosa:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    sys.exit(main())
