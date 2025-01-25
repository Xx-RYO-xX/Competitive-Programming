import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    k = []
    
    for i in range(n+1):
        
    
    print(*k, sep="\n")


if __name__ == '__main__':
    sys.exit(main())
