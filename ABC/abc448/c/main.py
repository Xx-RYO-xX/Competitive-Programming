import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b_to_a = []
    b_to_a.append(0)
    for A in a:
        b_to_a.append(A)
    a = SortedList(a)
    for _ in range(q):
        k = int(input())
        b = list(map(int, input().split()))
        for B in b:
            a.discard(b_to_a[B])
        print(a[0])
        for B in b:
            a.add(b_to_a[B])


if __name__ == "__main__":
    main()
