import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b, c = map(int, input().split())
    if a + b == a - b == c:
        print("?")
    elif a + b == c:
        print("+")
    elif a - b == c:
        print("-")
    else:
        print("!")


if __name__ == "__main__":
    main()
