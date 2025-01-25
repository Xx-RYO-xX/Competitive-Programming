import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    user = set()
    for i in range(1, n+1):
        s = input()
        if s not in user:
            user.add(s)
            print(i)


if __name__ == '__main__':
    sys.exit(main())
