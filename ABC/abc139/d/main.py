import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    ans = (n*(n-1))//2
    
    print(ans)


if __name__ == '__main__':
    main()
