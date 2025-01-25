import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())

    print(pow(10, n, m*m)//m % m)


if __name__ == '__main__':
    main()
