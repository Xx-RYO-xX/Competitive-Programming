def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = list(map(int, input().split()))

    print("Yes" if all([xx < 0 for xx in x]) else "No")


if __name__ == "__main__":
    main()
