import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    
    x = 0
    for i in range(m+1):
        x += n**i
    
    if x <= 10**9:
        print(x)
    else:
        print("inf")



if __name__ == '__main__':
    sys.exit(main())
