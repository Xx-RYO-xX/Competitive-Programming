import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    sp = []
    psum = 0
    for _ in range(n):
        s, p = input().split()
        p = int(p)
        sp.append((s, p))
        psum += p

    for s, p in sp:
        if p > psum / 2:
            print(s)
            return

    print("atcoder")


if __name__ == "__main__":
    main()
