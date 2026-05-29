import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = 2 * int(input())
    enn = [0] * (n + 2)
    ab = []
    for _ in range(n // 2):
        a, b = sorted(map(int, input().split()))
        enn[a] += 1
        enn[b + 1] -= 1
        ab.append([a, b])
    enn2 = [0]
    for e in enn[1:]:
        enn2.append(enn2[-1] + e)

    for a, b in ab:
        if enn2[a] != enn2[b]:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
