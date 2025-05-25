import sys


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c = input()
    print(int(a+b+c)+int(b+c+a)+int(c+a+b))


if __name__ == '__main__':
    main()
