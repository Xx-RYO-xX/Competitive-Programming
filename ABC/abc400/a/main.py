import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a = int(input())
    if 400 % a == 0:
        b = 400//a
        print(b)
    else:
        print(-1)


if __name__ == '__main__':
    sys.exit(main())
