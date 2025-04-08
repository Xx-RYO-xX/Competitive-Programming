import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = input()
    if "3" in n or int(n) % 3 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
