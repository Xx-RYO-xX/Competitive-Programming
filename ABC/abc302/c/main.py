import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations

    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(list(input()))

    for perm in permutations(s):
        cond = True
        for i in range(n - 1):
            diff = 0
            for j in range(m):
                if perm[i][j] != perm[i + 1][j]:
                    diff += 1
            if diff != 1:
                cond = False
                break
        if cond:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
