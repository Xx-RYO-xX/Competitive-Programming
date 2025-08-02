import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, a, b = map(int, input().split())
    s = input()
    
    if b == 0:
        print(s[a:])
    else:
        print(s[a:-b])


if __name__ == '__main__':
    main()
