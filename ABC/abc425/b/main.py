import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    used = set()
    for A in a:
        if A != -1:
            if A in used:
                print("No")
                return
            used.add(A)

    nouse = sorted(list(set(range(1, n + 1)) - used))

    p = []
    for A in a:
        if A == -1:
            p.append(nouse.pop())
        else:
            p.append(A)

    print("Yes")
    print(*p)


if __name__ == "__main__":
    main()
