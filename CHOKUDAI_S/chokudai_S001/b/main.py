import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))


if __name__ == '__main__':
    main()
