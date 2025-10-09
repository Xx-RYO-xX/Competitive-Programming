import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    x, y = input().split()
    os = ["Ocelot", "Serval", "Lynx"]

    if os.index(x) >= os.index(y):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
