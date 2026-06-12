import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()

    if n <= 7:
        print("Yes" if s[n - 1] == "o" else "No")

    else:
        print("Yes" if s[n - 1 - 7] == "o" else "No")


if __name__ == "__main__":
    main()
