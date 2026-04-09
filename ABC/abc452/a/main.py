import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    m, d = map(int, input().split())
    if m == d:
        if m == 3 or m == 5 or m == 7 or m == 9:
            print("Yes")
            return
    elif m == 1 and d == 7:
        print("Yes")
        return

    print("No")


if __name__ == "__main__":
    main()
