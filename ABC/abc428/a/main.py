import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s, a, b, x = map(int, input().split())

    byou = a + b

    print((x // byou) * s * a + s * min(x % byou, a))


if __name__ == "__main__":
    main()
