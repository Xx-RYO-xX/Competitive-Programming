def main():
    import sys

    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    from collections import Counter

    a = Counter(a)

    aval = list(a.values())

    print(aval.count(max(aval))+aval.count(max(aval)-1))

if __name__ == "__main__":
    main()
