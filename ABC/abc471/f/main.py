def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input()[:-1])
    print(sorted(s))


if __name__ == "__main__":
    main()
