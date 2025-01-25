import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        l, r = map(int, input().split())

if __name__ == '__main__':
    main()
