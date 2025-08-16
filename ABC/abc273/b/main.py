def main():
    from sys import stdin
    from decimal import Decimal, ROUND_HALF_UP

    readline = stdin.readline()

    x, k = map(int, readline.split())

    for i in range(1, k+1):
        x = Decimal(x).quantize(Decimal("1E"+str(i)), rounding=ROUND_HALF_UP)

    print(int(x))


if __name__ == "__main__":
    main()
