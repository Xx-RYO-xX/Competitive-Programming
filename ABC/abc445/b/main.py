import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = []
    m = 0
    for _ in range(n):
        st = input()
        m = max(m, len(st))
        s.append(st)

    for S in s:
        k = (m - len(S)) // 2
        print("." * k + S + "." * k)


if __name__ == "__main__":
    main()
