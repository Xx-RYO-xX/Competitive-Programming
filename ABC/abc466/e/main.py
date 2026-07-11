def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))


if __name__ == "__main__":
    main()
