import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    MOD = 10**9 +7
    print((pow(10, n, MOD)-(pow(9, n, MOD)+pow(9, n, MOD)-pow(8, n, MOD)))%MOD)

if __name__ == '__main__':
    main()
