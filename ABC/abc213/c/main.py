import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    h, w, n = map(int, input().split())
    a, b = [], []
    for _ in range(n):
        at, bt = map(int, input().split())
        a.append(at)
        b.append(bt)
    


if __name__ == '__main__':
    sys.exit(main())
