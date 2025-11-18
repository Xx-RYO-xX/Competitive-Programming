import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    abc = sorted(map(int, input().split()), reverse=True)

    print(*abc, sep="")


if __name__ == "__main__":
    main()
