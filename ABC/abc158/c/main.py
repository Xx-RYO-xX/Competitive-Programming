import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    
    for x in range(1, 10001):  
        if (x*8//100 == a) and (x*10//100 == b):
            print(x)
            return
    
    print(-1)


if __name__ == '__main__':
    sys.exit(main())
