def main():
    import sys

    input = sys.stdin.readline
    n = int(input())

    x = 10000
    y = 10000
    for _ in range(n):
        a, b, s = input().rstrip().split()
        a = int(a)
        b = int(b)

        x -= b
        y -= b
        if s == "take":
            x += b - a
        y += b - a

    print(y - x)


if __name__ == "__main__":
    main()
