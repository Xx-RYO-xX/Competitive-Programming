import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a = list(map(int, input().split()))
    print(a[0]*a[1]*a[2])


if __name__ == '__main__':
    main()
