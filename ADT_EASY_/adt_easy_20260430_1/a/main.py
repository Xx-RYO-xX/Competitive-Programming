import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    for S in s:
        if S == "2":
            print(S, end="")


if __name__ == "__main__":
    main()
