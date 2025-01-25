import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    k = 0
    while 2 ** k <= n:
        k += 1
    print(k - 1)

if __name__ == '__main__':
    main()
