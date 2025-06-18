import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    print(a-2*b if a-2*b >= 0 else 0)
    


if __name__ == '__main__':
    sys.exit(main())
