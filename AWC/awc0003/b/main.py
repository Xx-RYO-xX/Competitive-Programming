import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    lr = []
    for _ in range(n):
        l, r = input().split()
        lr.append((l, r))

    ans = 0
    for i in range(n - 1):
        if lr[i][1] == lr[i + 1][0]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
