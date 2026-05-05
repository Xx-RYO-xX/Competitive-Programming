import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import math

    a, b, h, m = map(int, input().split())

    if abs(30 * h - 5.5 * m) % 360 <= 180:
        print(
            math.sqrt(
                a**2
                + b**2
                - 2 * a * b * math.cos(math.radians(abs(30 * h - 5.5 * m) % 360))
            )
        )
    else:
        print(
            math.sqrt(
                a**2
                + b**2
                - 2 * a * b * math.cos(math.radians(360 - abs(30 * h - 5.5 * m) % 360))
            )
        )


if __name__ == "__main__":
    main()
