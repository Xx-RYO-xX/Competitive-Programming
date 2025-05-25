import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    x, y = 0, 0
    for _ in range(n):
        xt, yt = map(int, input().split())
        x += xt
        y += yt
    if x < y:
        print("Aoki")
    elif x > y :
        print("Takahashi")
    else:
        print("Draw")


if __name__ == '__main__':
    sys.exit(main())
