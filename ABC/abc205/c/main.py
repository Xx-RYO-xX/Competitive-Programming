import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c = map(int, input().split())
    c = 2 if c % 2 == 0 else 1
    if a**c < b**c :
        print("<")
    elif a**c == b**c:
        print("=")
    else:
        print(">")


if __name__ == '__main__':
    sys.exit(main())
