import sys


def input():return sys.stdin.readline().rstrip()


def main():
    a, b = input().split()
    print(max(sum(int(i) for i in list(a)), sum(int(i) for i in list(b))))


if __name__ == '__main__':
    main()
