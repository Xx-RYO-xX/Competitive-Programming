import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print([A%2 != 0 for A in a].count(True))
    


if __name__ == '__main__':
    sys.exit(main())
