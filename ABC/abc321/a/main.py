import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = input()
    for i in range(len(n) - 1):
        if n[i] <= n[i + 1]:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    sys.exit(main())
