import sys


def input():return sys.stdin.readline().rstrip()


def main():
    abcde = set(map(int, input().split()))
    print(len(abcde))

if __name__ == '__main__':
    main()
