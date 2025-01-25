import sys


def input():return sys.stdin.readline().rstrip()


def main():
    t = int(input())
    for i in range(1, t+1):
        print("Case #%d:" %i)
        print("Hello World!")

if __name__ == '__main__':
    main()
