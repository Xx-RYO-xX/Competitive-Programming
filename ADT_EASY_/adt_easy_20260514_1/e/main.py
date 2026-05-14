import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    accm = [0] + list(accumulate(a * 2))

    start = 0
    for _ in range(q):
        que = input()
        if que[0] == "1":
            num, c = map(int, que.split())
            start = (start + c) % n
        else:
            num, l, r = map(int, que.split())
            ans = accm[start + r] - accm[start + l - 1]
            print(ans)


if __name__ == "__main__":
    main()
