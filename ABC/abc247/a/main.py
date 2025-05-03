import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    print("0"+s[:-1])


if __name__ == '__main__':
    sys.exit(main())
