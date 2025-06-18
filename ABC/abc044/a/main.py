import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())

    ans = 0
    for i in range(n):
        if i < k:
            ans += x
        else:
            ans += y

    print(ans)


if __name__ == '__main__':
    sys.exit(main())
