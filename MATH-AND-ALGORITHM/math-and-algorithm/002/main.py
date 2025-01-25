import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a = list(map(int, input().split()))
    print(sum(a))


if __name__ == '__main__':
    main()
