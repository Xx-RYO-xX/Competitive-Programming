import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from fractions import Fraction
    
    n = int(input())
    a = list(map(int, input().split()))
    
    if n < 3:
        print("Yes")
        return
        
    
    r = Fraction(a[1], a[0])
    for i in range(1, n):
        if a[i - 1] * r != a[i]:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    sys.exit(main())
