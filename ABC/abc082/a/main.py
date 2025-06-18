import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    ab = a+b
    
    if ab % 2 == 0:
        print(ab//2)
    else:
        print(ab//2+1)


if __name__ == '__main__':
    sys.exit(main())
