import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    for _ in range(int(input())):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        print(
            "Yes"
            if (r1 - r2) ** 2 <= (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2
            else "No"
        )


if __name__ == "__main__":
    main()
