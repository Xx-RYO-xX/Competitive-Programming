import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = list(input())

    s_ten = [num for num, chr in enumerate(s) if chr == "A"]

    aba = 0
    bab = 0

    for i in range(n):
        aba += abs(s_ten[i] - (2 * i))
        bab += abs(s_ten[i] - (2 * i + 1))

    print(min(aba, bab))


if __name__ == "__main__":
    main()
