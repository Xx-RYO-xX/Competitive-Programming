import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    moji = set()
    for _ in range(n):
        s = input()
        if s[0] not in {"H", "D", "C", "S"}:
            print("No")
            return
        if s[1] not in {
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "T",
            "J",
            "Q",
            "K",
        }:
            print("No")
            return
        if s in moji:
            print("No")
            return
        moji.add(s)
    print("Yes")


if __name__ == "__main__":
    main()
