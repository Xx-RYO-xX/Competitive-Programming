import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    t = []
    for _ in range(n):
        t.append(int(input()))
    print(min(t))


if __name__ == '__main__':
    sys.exit(main())
