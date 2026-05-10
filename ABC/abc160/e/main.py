import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x, y, a, b, c = map(int, input().split())
    p = sorted(map(int, input().split()), reverse=True)
    q = sorted(map(int, input().split()), reverse=True)
    r = sorted(map(int, input().split()))

    pqr = p[:x] + q[:y] + r
    pqr.sort(reverse=True)

    print(sum(pqr[: x + y]))


if __name__ == "__main__":
    main()
