import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, w, k = map(int, input().split())
    print("Yes" if w/(n-1) >=k else "No")
    


if __name__ == '__main__':
    main()
