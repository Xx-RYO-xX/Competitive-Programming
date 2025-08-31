import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    man = dict()
    for i in range(n):
        s = input()
        man[i + 1] = s
    x, y = input().split()
    print("Yes" if man[int(x)] == y else "No")


if __name__ == "__main__":
    main()
