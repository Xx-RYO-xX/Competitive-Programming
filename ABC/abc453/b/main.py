import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    t, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    for tt in range(t + 1):
        aa = a[tt]
        if tt == 0:
            ans.append((tt, aa))
        else:
            if abs(aa - ans[-1][1]) >= x:
                ans.append((tt, aa))

    for ANS in ans:
        print(*ANS)


if __name__ == "__main__":
    main()
