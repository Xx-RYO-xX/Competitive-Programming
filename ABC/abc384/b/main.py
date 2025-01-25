import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, r = map(int, input().split())
    for _ in range(n):
        d, a = map(int, input().split())
        if d == 1 and 1600 <= r <= 2799:
            r += a
        elif d == 2 and 1200 <= r <= 2399:
            r += a
    
    print(r)


if __name__ == '__main__':
    main()
