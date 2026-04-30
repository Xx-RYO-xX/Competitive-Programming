import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from scipy.optimize import bisect

    a, b, x = map(int, input().split())

    def f(n):
        return x - (a * n + b * len(str(int(n))))

    if f(1) < 0:
        print(0)
        return

    try:

        anst = int(bisect(f, 0, 10**9))
        ans = 0

        for i in range(anst - 3, anst + 3):
            if 1 <= i <= 10**9 and x >= (a * i + b * len(str(i))):
                ans = max(ans, i)
        print(ans)
    except:
        print(10**9)


if __name__ == "__main__":
    main()
