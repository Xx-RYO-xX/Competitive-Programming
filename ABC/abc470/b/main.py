def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = list(map(int, input().split()))

    from collections import Counter

    print(n - c.count(max(Counter(c).items(), key=lambda x: x[1])[0]))


if __name__ == "__main__":
    main()
