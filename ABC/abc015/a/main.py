import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a = input()
    b = input()

    print(a if len(a) > len(b) else b)


if __name__ == "__main__":
    main()
