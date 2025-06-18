import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    x, y = input().split()
    
    if x < y:
        print("<")
    elif x > y:
        print(">")
    else:
        print("=")


if __name__ == '__main__':
    sys.exit(main())
