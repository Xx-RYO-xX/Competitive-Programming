import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    print("Yes" if x in a else "No")
    

if __name__ == '__main__':
    main()
