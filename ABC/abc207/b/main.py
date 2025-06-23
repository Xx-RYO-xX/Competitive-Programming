import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from time import time
    a, b, c, d = map(int, input().split())
    start = time()
    
    i = 0
    red = 0
    while time()-start < 1.9:
        if a <= red*d:
            print(i)
            return
        a += b
        red += c
        i += 1
    
    print(-1)


if __name__ == '__main__':
    main()
