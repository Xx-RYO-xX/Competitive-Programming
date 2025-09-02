import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())

    ab = (xa - xb) ** 2 + (ya - yb) ** 2
    bc = (xb - xc) ** 2 + (yb - yc) ** 2
    ca = (xc - xa) ** 2 + (yc - ya) ** 2

    if ab + bc == ca or bc + ca == ab or ca + ab == bc:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
