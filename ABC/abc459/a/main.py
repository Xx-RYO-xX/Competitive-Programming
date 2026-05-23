import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x = int(input())
    h = list("HelloWorld")
    for i in range(len(h)):
        if i != x - 1:
            print(h[i], end="")


if __name__ == "__main__":
    main()
