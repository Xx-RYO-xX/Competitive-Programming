import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    for _ in range(int(input())):
        a, b, x, y = map(lambda x: abs(int(x)), input().split())
        nanaame = min(2 * a, 2 * b)
        chokusen = min(a + b, 2 * nanaame)

        if (x + y) % 2 == 0:
            print(min(x, y) * nanaame + (max(x, y) - min(x, y)) // 2 * chokusen)
        else:
            ans1 = (
                min(x - 1, y) * nanaame
                + (max(x - 1, y) - min(x - 1, y)) // 2 * chokusen
                + a
            )
            ans2 = (
                min(x, y - 1) * nanaame
                + (max(x, y - 1) - min(x, y - 1)) // 2 * chokusen
                + b
            )
            print(min(ans1, ans2))


if __name__ == "__main__":
    main()
