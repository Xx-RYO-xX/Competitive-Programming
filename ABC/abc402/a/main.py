import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    ans = ''.join([c for c in s if c.isupper()])
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
