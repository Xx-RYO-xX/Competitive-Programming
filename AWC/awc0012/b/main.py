import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, t, c, d = map(int, input().split())
    w = list(map(int, input().split()))

    cnt = 0
    for W in w:
        if t <= W:
            cnt += 1
    print(min(c * cnt, d * cnt))


if __name__ == "__main__":
    main()
