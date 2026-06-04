import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations

    s, k = input().split()
    k = int(k)

    ans = set()
    for perm in permutations(s):
        ans.add("".join(perm))

    print(sorted(ans)[k - 1])


if __name__ == "__main__":
    main()
