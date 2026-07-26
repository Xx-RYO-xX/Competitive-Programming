def main():
    import sys

    input = sys.stdin.readline

    from fractions import Fraction

    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for A in a:
        ans += Fraction(1, A)

    ans = Fraction(1, ans)

    print(float(ans))


if __name__ == "__main__":
    main()
