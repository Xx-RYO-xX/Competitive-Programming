import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    for i in range(2, n + 1)[::-1]:
        print(i, end=",")
    print(1)


if __name__ == "__main__":
    main()
