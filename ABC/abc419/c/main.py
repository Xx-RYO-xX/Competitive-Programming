import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import math
    n = int(input())
    r, c = [], []
    for _ in range(n):
        rt, ct = map(int, input().split())
        r.append(rt)
        c.append(ct)

    ans = math.ceil(max(max(r)-min(r), max(c)-min(c))/2)
    print(ans)


if __name__ == '__main__':
    main()
