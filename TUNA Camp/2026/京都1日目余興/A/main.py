import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations

    s = input()
    for perm in permutations(s):
        perm = "".join(perm)
        if perm == "TUNA":
            print("MAGURO")
        if perm == "CAMP":
            print("YAEI")


if __name__ == "__main__":
    main()
