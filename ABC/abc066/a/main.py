import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    print(sum(sorted(map(int, input().split()))[:2]))


if __name__ == '__main__':
    sys.exit(main())
