def main():
    a, b, c, d = map(int, input().split())

    if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()