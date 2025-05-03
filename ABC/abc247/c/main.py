import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    def s(n):
        if n == 1:
            return [1]
        else:
            return s(n-1)+[n]+s(n-1)
    print(*s(n))


if __name__ == '__main__':
    sys.exit(main())
