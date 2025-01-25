import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    
    print(c.index(a+b)+1)


if __name__ == '__main__':
    main()
