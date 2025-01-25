import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print(sum(map(int, input().split())))


if __name__ == '__main__':
    main()
