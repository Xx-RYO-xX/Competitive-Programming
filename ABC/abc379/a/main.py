import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = list(input())
    a, b, c = map(str, n)
    print(b+c+a, c+a+b)
    


if __name__ == '__main__':
    main()
