import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    x = float(input())
    if x < 37.5:
        print(3)
    elif 37.5 <= x < 38:
        print(2)
    else:
        print(1)


if __name__ == '__main__':
    sys.exit(main())
