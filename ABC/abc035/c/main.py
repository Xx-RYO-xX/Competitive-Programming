import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    retu = [0] * (n + 1)
    for _ in range(q):
        l, r = map(int, input().split())
        retu[l - 1] += 1
        retu[r] -= 1

    ans = 0
    for i in range(n):
        ans += retu[i]
        print(ans % 2, end="")
    print()


if __name__ == "__main__":
    main()
