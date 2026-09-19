def main():
    import sys

    input = sys.stdin.readline
    s = input()[:-1]
    for i in range(len(s)-1):
        print(s[i]+"o", end="")

    print(s[-1])

if __name__ == "__main__":
    main()
