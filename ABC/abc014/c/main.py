import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    color = [0] * 1000002
    for _ in range(n):
        a, b = map(int, input().split())
        color[a] += 1
        color[b + 1] -= 1

    ans = 0
    now = 0
    for i in range(1000001):
        now += color[i]
        ans = max(ans, now)

    print(ans)


if __name__ == "__main__":
    main()
