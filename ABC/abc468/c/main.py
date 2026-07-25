def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    lst = [i for i in range(1, n + 1)]

    from itertools import permutations

    ans = 0
    for perm in permutations(lst):
        if p < list(perm) < q:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
