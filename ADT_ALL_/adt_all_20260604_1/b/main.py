import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter

    n = int(input())
    s = input()
    sc = Counter(s)
    if sc["T"] > sc["A"]:
        print("T")
    elif sc["T"] < sc["A"]:
        print("A")
    else:
        print("A" if s[-1] == "T" else "T")


if __name__ == "__main__":
    main()
