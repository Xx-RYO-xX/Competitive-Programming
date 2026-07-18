def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())

    print("Yes" if w * 10000 / h / h >= 25 else "No")


if __name__ == "__main__":
    main()
