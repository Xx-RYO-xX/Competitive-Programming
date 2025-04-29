import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from math import sqrt
    txa, tya, txb, tyb, t, v = map(int, input().split())
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        uwaki = 0
        uwaki += sqrt((txa-x)**2+(tya-y)**2)
        uwaki += sqrt((txb-x)**2+(tyb-y)**2)
        if uwaki <= t*v:
            print("YES")
            exit()
    print("NO")


if __name__ == '__main__':
    main()
