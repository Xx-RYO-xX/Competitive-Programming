import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = int(input())

    print("Yes" if len(s) % 5 == 0 else "No")


if __name__ == "__main__":
    main()
