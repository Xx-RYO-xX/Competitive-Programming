import sys


def input():return sys.stdin.readline().rstrip()


def main():
    a = int(input())
    b = int(input())
    n = int(input())
    while True:
        if n % a == 0 and n % b == 0:
            print(n)
            break
        n += 1


if __name__ == '__main__':
    main()
