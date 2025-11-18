import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations

    x = input()

    ans = float("inf")
    for num in permutations(x, len(x)):
        if num[0] == "0":
            continue

        ans = min(ans, (int("".join(num))))

    print(ans)


if __name__ == "__main__":
    main()
