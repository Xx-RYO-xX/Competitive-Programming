import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    i = int(input())
    print(s[i-1])

if __name__ == '__main__':
    main()
