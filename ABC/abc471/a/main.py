def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    print("Nine" if a + b == 9 or a - b == 9 or a * b == 9 or a / b == 9 else "Nein")


if __name__ == "__main__":
    main()
