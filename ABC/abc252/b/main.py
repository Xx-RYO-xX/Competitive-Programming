import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = set(map(int, input().split()))

    oisi = [i for i, ai in enumerate(a, 1) if ai == max(a)]

    for aa in oisi:
        if aa in b:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
