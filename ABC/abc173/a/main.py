import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    ans = ((n+999)//1000)*1000-n
    print(ans)


if __name__ == '__main__':
    main()
