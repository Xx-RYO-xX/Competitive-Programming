import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    b = int(input())

    for a in range(1, 20):
        if a**a == b:
            print(a)
            return
    print(-1)


if __name__ == "__main__":
    main()
