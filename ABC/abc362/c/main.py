import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ans = 0
    l, r = [], []
    for i in range(n):
        lt, rt = map(int, input().split())
        l.append(lt)
        r.append(rt)
        ans += lt

    if 0 < ans:
        print("No")
        return

    for i in range(n):
        li, ri = l[i], r[i]
        ans -= li
        ans += ri
        if 0 <= ans:
            print("Yes")

            ansi = ri - ans
            print(*r[:i], ansi, *l[i + 1 :])
            return

    print("No")
    return


if __name__ == "__main__":
    main()
