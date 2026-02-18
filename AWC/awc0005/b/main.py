import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, k = map(int, input().split())
    s = list(map(int, input().split()))
    ss = dict()
    for num, item in enumerate(s, 1):
        ss[num] = item
    for _ in range(m):
        p, v = map(int, input().split())
        ss[p] = v

    print(sum([item < k for num, item in ss.items()]))


if __name__ == "__main__":
    main()
