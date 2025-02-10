import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations
    a = list(map(int, input().split()))

    for A in permutations(a):
        if A[0] * A[1] == A[2]:
            print("Yes")
            return

    print("No")


if __name__ == '__main__':
    sys.exit(main())
