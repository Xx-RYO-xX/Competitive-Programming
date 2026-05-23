import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = list(input().split())

    for i in range(n):
        ss = s[i][0]

        if "a" <= ss <= "c":
            print(2, end="")
        elif "d" <= ss <= "f":
            print(3, end="")
        elif "g" <= ss <= "i":
            print(4, end="")
        elif "j" <= ss <= "l":
            print(5, end="")
        elif "m" <= ss <= "o":
            print(6, end="")
        elif "p" <= ss <= "s":
            print(7, end="")
        elif "t" <= ss <= "v":
            print(8, end="")
        elif "w" <= ss <= "z":
            print(9, end="")


if __name__ == "__main__":
    main()
