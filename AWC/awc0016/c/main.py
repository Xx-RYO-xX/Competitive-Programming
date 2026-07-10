import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, l, r, t = map(int, input().split())
    ans = []
    for i in range(n):
        p, s = map(int, input().split())
        if l <= p <= r and t <= s:
            ans.append((p, s, i))

    ans.sort(key=lambda x: (x[0], -x[1], x[2]))

    print(ans[0][2] + 1 if ans else -1)


if __name__ == "__main__":
    main()
