import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = set(map(int, input().split()))

    ans = []
    for i in range(1, n+1):
        if i not in a:
            ans.append(i)

    print(len(ans))
    print(*ans, sep=" ")


if __name__ == '__main__':
    sys.exit(main())
