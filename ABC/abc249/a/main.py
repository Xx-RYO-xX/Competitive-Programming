import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c, d, e, f, x = map(int, input().split())
    
    takahashi = 0
    aoki = 0
    for i in range(x):
        if i % (a+c) < a:
            takahashi += b
        if i % (d+f) < d:
            aoki += e
    
    if takahashi > aoki:
        print("Takahashi")
    elif aoki > takahashi:
        print("Aoki")
    else:
        print("Draw")


if __name__ == '__main__':
    sys.exit(main())
