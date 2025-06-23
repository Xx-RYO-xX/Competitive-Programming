import sys


def input():return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    print("Yes" if a <=  b <= 6*a else "No")
    


if __name__ == '__main__':
    main()
