import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    sunuke = []
    for _ in range(n):
        t, x, a = map(int, input().split())
        sunuke.append((t, x, a))
    
    sunuke.sort()


if __name__ == '__main__':
    sys.exit(main())
