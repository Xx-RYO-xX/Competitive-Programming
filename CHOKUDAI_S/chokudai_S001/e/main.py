import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    print(a.index(1)+1)


if __name__ == '__main__':
    main()
