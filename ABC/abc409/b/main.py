import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    ans = 0
    for i, v in enumerate(a):
        if v >= i + 1:
            ans = i + 1
        else:
            break

    print(ans)


if __name__ == '__main__':
    main()
