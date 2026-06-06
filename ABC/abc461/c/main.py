import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k, m = map(int, input().split())
    c_v = [[] for _ in range(n + 1)]

    for _ in range(n):
        c, v = map(int, input().split())
        c_v[c].append(v)

    max_v = []
    two_v = []

    for i in range(1, n + 1):
        if c_v[i]:
            c_v[i].sort(reverse=True)
            max_v.append(c_v[i][0])
            two_v.extend(c_v[i][1:])

    max_v.sort(reverse=True)
    ans = sum(max_v[:m])
    two_v.extend(max_v[m:])
    two_v.sort(reverse=True)

    ans += sum(two_v[: k - m])

    print(ans)


if __name__ == "__main__":
    main()
