import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c = map(int, input().split())
    
    if a < c < b or b < c < a:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    sys.exit(main())
