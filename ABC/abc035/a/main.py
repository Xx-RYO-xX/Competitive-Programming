import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import gcd

    w, h = map(int, input().split())
    gc = gcd(w, h)

    if w // gc == 4 and h // gc == 3:
        print("4:3")
    else:
        print("16:9")


if __name__ == "__main__":
    main()
