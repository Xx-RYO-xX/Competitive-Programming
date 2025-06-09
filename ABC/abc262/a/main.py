import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    y = int(input())
    for i in range(y, 100000):
        if i % 4 == 2:
            print(i)
            return


if __name__ == '__main__':
    sys.exit(main())
