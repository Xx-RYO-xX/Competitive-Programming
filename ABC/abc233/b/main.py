import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    l, r = map(int, input().split())
    s = list(input())

    s[l-1:r] = s[l-1:r][::-1]

    print(*s, sep="")

if __name__ == '__main__':
    sys.exit(main())
