import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x, y = input().split(".")
    if 0 <= int(y) <= 2:
        print(x + "-")
    elif 3 <= int(y) <= 6:
        print(x)
    else:
        print(x + "+")


if __name__ == "__main__":
    main()
