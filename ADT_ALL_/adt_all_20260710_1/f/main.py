import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = sorted(set(map(int, input().split())))
    ans = k * (k + 1) // 2
    minus = 0
    for A in a:
        if A <= k:
            minus += A
        else:
            break
    # print(ans, minus)
    print(ans - minus)


if __name__ == "__main__":
    main()
