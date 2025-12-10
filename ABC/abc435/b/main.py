import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for l in range(n):
        sums = 0
        for r in range(l, n):
            sums += a[r]
            cond = True
            for i in range(l, r + 1):
                if sums % a[i] == 0:
                    cond = False
                    break
            if cond:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
