import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    nedan = int(1.08*n)
    if nedan < 206:
        print("Yay!")
    elif nedan == 206:
        print("so-so")
    else:
        print(":(")


if __name__ == '__main__':
    main()
