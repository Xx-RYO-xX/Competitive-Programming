import sys


def input():
    return sys.stdin.readline().rstrip()


def cnt_guusuu(num1, num2):
    ans = num2 // 2 - (num1 - 1) // 2
    return ans if ans > 0 else 0


def solve(l, r, y):
    yy = abs(y)
    ans = 0

    ans += cnt_guusuu(l, min(r, -yy - 1))
    ans += cnt_guusuu(max(l, yy + 1), r)

    if yy % 2 == 0:
        left = max(l, -yy)
        right = min(r, yy)
        if left <= right:
            ans += right - left + 1

    return ans


def main():
    l, r, d, u = map(int, input().split())
    ans = 0
    for y in range(d, u + 1):
        ans += solve(l, r, y)

    print(ans)


if __name__ == "__main__":
    main()
