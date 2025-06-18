import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, a, b = map(int, input().split())

    ans = (n//(a+b))*a + min(a, n%(a+b))

    print(ans)

if __name__ == '__main__':
    sys.exit(main())
