import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    L, R = 1, 2

    def kaitenn(start, end, kabe):

        ans1 = 0
        ans_lst = []
        nex_lst = [((start + i) % n) + 1 for i in range(n)]
        for nex in nex_lst:
            if nex == kabe:
                break
            ans1 += 1
            if nex == end:
                ans_lst.append(ans1)

        ans2 = 0
        for nex in nex_lst[::-1]:
            if nex == kabe:
                break
            ans2 += 1
            if nex == end:
                ans_lst.append(ans2 - 1)

        return min(ans_lst)

    ans = 0
    for _ in range(q):
        h, t = input().split()
        t = int(t)
        if h == "L":
            # print(kaitenn(L, t, R))
            ans += kaitenn(L, t, R)
            L = t
        else:
            # print(kaitenn(R, t, L))
            ans += kaitenn(R, t, L)
            R = t

    print(ans)


if __name__ == "__main__":
    main()
