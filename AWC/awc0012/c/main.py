import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k, m = map(int, input().split())
    keikenn = []
    shoshinnsha = []
    for _ in range(n):
        h, p = map(int, input().split())
        if h:
            keikenn.append(p)
        else:
            shoshinnsha.append(p)

    if len(keikenn) < m or len(shoshinnsha) < k - m:
        print(-1)
        return

    keikenn.sort(reverse=True)
    shoshinnsha.sort(reverse=True)
    ans = 0
    for i in range(m):
        ans += keikenn[i]
    for i in range(k - m):
        ans += shoshinnsha[i]

    print(ans)


if __name__ == "__main__":
    main()
