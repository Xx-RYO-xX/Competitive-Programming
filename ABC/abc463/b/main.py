import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, x = input().split()
    n = int(n)
    s = []
    for _ in range((n)):
        s.append(input())

    AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Yes" if "o" in [s[i][AZ.index(x)] for i in range(n)] else "No")


if __name__ == "__main__":
    main()
