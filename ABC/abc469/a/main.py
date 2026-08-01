def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    print(n - k + 1)


if __name__ == "__main__":
    main()
