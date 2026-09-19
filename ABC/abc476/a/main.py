def main():
    import sys

    input = sys.stdin.readline
    s = list(input())[:-1]

    if s[-1] == "e":
        print(*s, sep="", end="")
        print("r")
    else:
        print(*s, sep="", end="")
        print("er")

if __name__ == "__main__":
    main()
