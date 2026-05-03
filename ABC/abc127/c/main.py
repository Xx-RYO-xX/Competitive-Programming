import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    kukan = [0] * (n + 1)
    for _ in range(m):
        l, r = map(lambda x: int(x) - 1, input().split())
        kukan[l] += 1
        kukan[r + 1] -= 1

    ans = 0
    gate = 0
    for i in range(n):
        gate += kukan[i]
        if gate == m:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
