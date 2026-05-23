import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, q = map(int, input().split())
    min_cnt = 0
    masu = [0] * n
    kosuu = defaultdict(int)
    kosuu[0] = n
    for _ in range(q):
        num, xy = map(int, input().split())
        if num == 1:
            x = xy - 1
            masu[x] += 1
            kosuu[masu[x]] += 1
            if kosuu[min_cnt + 1] == n:
                min_cnt += 1
        else:
            y = xy
            print(kosuu[y + min_cnt])


if __name__ == "__main__":
    main()
