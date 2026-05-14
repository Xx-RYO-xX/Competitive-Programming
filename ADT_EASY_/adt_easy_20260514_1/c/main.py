import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = []
    maxs = 0
    for i in range(n):
        st = input()
        s.append(st)
        maxs = max(maxs, len(st))

    for S in s:
        k = (maxs - len(S)) // 2
        print("." * k + S + "." * k)


if __name__ == "__main__":
    main()
