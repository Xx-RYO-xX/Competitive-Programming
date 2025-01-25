import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c, d, e, f = map(int, input().split())
    
    print(((a*b*c)-(d*e*f))%998244353)


if __name__ == '__main__':
    sys.exit(main())
