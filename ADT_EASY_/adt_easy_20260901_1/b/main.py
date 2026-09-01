def main():
    import sys

    input = sys.stdin.readline
    s = input()[:-1]

    if s[-2:]=="er":
        print("er")
    else:
        print("ist")

if __name__ == "__main__":
    main()
