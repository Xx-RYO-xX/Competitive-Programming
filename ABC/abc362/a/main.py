import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    r, g, b = map(int, input().split())
    c = input()

    if c == "Red":
        print(min(g, b))
    elif c == "Green":
        print(min(r, b))
    else:
        print(min(r, g))


if __name__ == "__main__":
    main()
