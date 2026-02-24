import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(list(input()))

    ans = set()
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            ss = []
            for ii in range(i, i + m):
                for jj in range(j, j + m):
                    ss.append(s[ii][jj])
            ans.add(tuple(ss))

    print(len(ans))


if __name__ == "__main__":
    main()
