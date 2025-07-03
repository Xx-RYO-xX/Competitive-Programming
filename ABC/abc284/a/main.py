import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(*s[::-1], sep="\n")


if __name__ == '__main__':
    sys.exit(main())
