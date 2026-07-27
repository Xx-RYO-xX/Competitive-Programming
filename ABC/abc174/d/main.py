def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input())[:-1]

    wcnt = s.count("W")

    # print(s[wcnt:])
    wcnt_l = s[:wcnt].count("W")

    print(wcnt_l)


if __name__ == "__main__":
    main()
