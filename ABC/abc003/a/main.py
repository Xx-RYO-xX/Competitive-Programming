import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += i*10**4
    print(ans//n)

if __name__ == '__main__':
    main()
