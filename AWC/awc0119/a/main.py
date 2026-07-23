def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = set(map(int, input().split()))

    print(len(s), sum(s))


if __name__ == "__main__":
    main()
