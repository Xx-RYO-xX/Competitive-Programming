import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, r, l = map(int, input().split())
    p = sorted(
        [(x, i) for i, x in enumerate(map(int, input().split()), start=1)], reverse=True
    )

    ans = []
    maxx = 0

    for P in p:
        x, i = P
        if r <= x <= l and maxx <= x:
            ans.append(i)
            maxx = x
    print(min(ans) if len(ans) != 0 else -1)


if __name__ == "__main__":
    main()
