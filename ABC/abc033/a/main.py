import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = input()
    print("SAME" if n[0] == n[1] == n[2] == n[3] else "DIFFERENT")


if __name__ == "__main__":
    main()
