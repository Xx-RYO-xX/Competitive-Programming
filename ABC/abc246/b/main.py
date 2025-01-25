import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import math
    a, b = map(int, input().split())
    d = math.sqrt(a**2 + b**2)
    print(a/d, b/d)


if __name__ == '__main__':
    sys.exit(main())
