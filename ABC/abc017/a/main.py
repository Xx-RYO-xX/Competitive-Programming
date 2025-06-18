import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    ans = 0
    for _ in range(3):
        a, b = map(int, input().split())
        ans += a * b // 10
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
