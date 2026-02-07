import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import re

    n, m = map(int, input().split())
    s = "^[" + input() + "]+$"
    t = "^[" + input() + "]+$"
    takahashi = re.compile(s)
    aoki = re.compile(t)
    for _ in range(int(input())):
        w = input()
        if takahashi.match(w) and aoki.match(w):
            print("Unknown")
        elif takahashi.match(w):
            print("Takahashi")
        elif aoki.match(w):
            print("Aoki")
        else:
            print("Unknown")


if __name__ == "__main__":
    main()
