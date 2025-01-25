import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print((a//b) if a*b > 0 else -(-a//b))


if __name__ == '__main__':
    main()
