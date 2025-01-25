import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = input()
    print(t.upper() if s == "Y" else t)


if __name__ == '__main__':
    main()
