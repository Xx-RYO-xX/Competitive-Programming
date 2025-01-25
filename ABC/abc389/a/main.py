import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    print(int(s[0])*int(s[-1]))


if __name__ == '__main__':
    sys.exit(main())
