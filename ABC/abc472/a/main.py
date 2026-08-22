def main():
    import sys

    input = sys.stdin.readline

    s = list(input())[:-1]

    for S in s:
        if S != "A":
            print(".", end="")
        else:
            print(S, end="")


if __name__ == "__main__":
    main()
