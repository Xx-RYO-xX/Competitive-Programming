import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = input()
    if n[-1] != "9":
        print(int(n) + 1)
    else:
        print("1" + n)


if __name__ == "__main__":
    main()
