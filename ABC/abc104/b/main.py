import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    n = len(s)
    i, j = sorted((2, n - 2))
    if s[0] == "A":
        if s[i : j + 1].count("C") == 1:
            idx = s[i : j + 1].index("C") + i
            for i in range(1, n):
                if i != idx and s[i].isupper():
                    break
            else:
                print("AC")
                return
    print("WA")


if __name__ == "__main__":
    main()
