import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h = int(input())
    takasa = 0
    i = 0
    while takasa < h:
        i += 1
        takasa += 2**i
    print(i + 1)


if __name__ == "__main__":
    main()
