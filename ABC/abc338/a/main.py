import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    print(
        "Yes"
        if s[0].isupper() and all([s[i].islower() for i in range(1, len(s))])
        else "No"
    )


if __name__ == "__main__":
    main()
