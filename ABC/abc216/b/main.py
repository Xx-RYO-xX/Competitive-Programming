import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    name = set()
    for _ in range(n):
        s, t = input().split()
        namet = s + " " + t
        if namet in name:
            print("Yes")
            return
        else:
            name.add(namet)

    print("No")


if __name__ == "__main__":
    main()
