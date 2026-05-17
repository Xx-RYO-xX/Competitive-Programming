import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    cd = []
    for _ in range(m):
        c, d = map(int, input().split())
        cd.append((c, d))

    for i in range(n):
        a, b = ab[i]
        minL = float("inf")
        ans = 0
        for j in range(m):
            c, d = cd[j]
            man = abs(a - c) + abs(b - d)
            if minL > man:
                minL = man
                ans = j + 1
        print(ans)


if __name__ == "__main__":
    main()
