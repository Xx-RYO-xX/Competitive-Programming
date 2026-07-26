def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)

    for _ in range(n - 1):
        x = a.pop()
        y = a.pop()
        a.append((x + y) / 2)

    print(*a)


if __name__ == "__main__":
    main()
