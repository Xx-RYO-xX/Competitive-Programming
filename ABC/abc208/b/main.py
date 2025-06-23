import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from math import factorial
    p = int(input())
    
    ans = 0
    for i in range(1, 11)[::-1]:
        coin = factorial(i)
        siharai = min(p//coin, 100)
        ans += siharai
        p -= coin*siharai
    print(ans)


if __name__ == '__main__':
    main()
