import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    n = int(input())
    ans = [0, 0]
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            ans[0] += 1
            ans[1] += a - b

    print(*ans)


if __name__ == "__main__":
    main()
