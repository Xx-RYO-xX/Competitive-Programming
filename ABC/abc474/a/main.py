def main():
    import sys

    input = sys.stdin.readline
    x = int(input())
    x += 1
    if x > 3:
        x = 1
    print(x)


if __name__ == "__main__":
    main()
