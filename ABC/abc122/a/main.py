import sys


def input():return sys.stdin.readline().rstrip()


def main():
    b = input()
    ACTG = "ACTG"
    print(ACTG[(ACTG.index(b)+2)%4])


if __name__ == '__main__':
    main()
