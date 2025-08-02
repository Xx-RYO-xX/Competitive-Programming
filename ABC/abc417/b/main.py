import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for i in range(m):
        try:
            a.remove(b[i])
        except:
            continue
    
    print(*a)


if __name__ == '__main__':
    main()
