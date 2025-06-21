import sys


def input():return sys.stdin.readline().rstrip()


def main():
    p = input()
    l = int(input())

    print("Yes" if len(p) >= l else "No")
    


if __name__ == '__main__':
    main()
