import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())

    ans = round(a/b)
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
