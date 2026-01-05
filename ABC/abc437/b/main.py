import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w, n = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))
    ans = [0] * h
    for _ in range(n):
        b = int(input())
        for i in range(h):
            if b in a[i]:
                ans[i] += 1

    print(max(ans))


if __name__ == "__main__":
    main()
