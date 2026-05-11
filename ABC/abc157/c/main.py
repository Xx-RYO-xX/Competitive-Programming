import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    num = [None] * (n + 1)
    for _ in range(m):
        s, c = map(int, input().split())
        if n > 1 and s == 1 and c == 0:
            print(-1)
            return
        if num[s] != None and num[s] != c:
            print(-1)
            return
        num[s] = c
    for i in range(1, n + 1):
        if num[i] == None:
            num[i] = 1 if n > 1 and i == 1 else 0

    print(*num[1:], sep="")


if __name__ == "__main__":
    main()
