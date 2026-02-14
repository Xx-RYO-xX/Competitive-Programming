import sys


def input():
    return sys.stdin.readline().rstrip()


def bit_full_search(lst, n):
    """
    ビット全探索する関数だっピ\n
    ￣￣V￣￣￣￣￣￣￣￣￣￣￣\n
    ( ・3・)\n
    /｜｜｜\\

    Parameters
    ----------
    lst : list
        ビット全探索したいリスト
    n : int
        リストの要素数

    Returns
    -------
    return : list
        ビット全探索した結果のリスト
    """
    ans = []
    for i in range(2**n):
        s_u_m = []
        for j in range(n):
            bit = 2**j
            if (i // bit) % 2 == 1:
                s_u_m.append(lst[j])
        ans.append(sum(s_u_m))

    return ans


def main():
    from bisect import bisect_left, bisect_right

    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    ans1 = bit_full_search(a[: n // 2], len(a[: n // 2]))
    ans2 = bit_full_search(a[n // 2 :], len(a[n // 2 :]))
    ans1.sort()
    ans2.sort()

    ans = 0
    for aa in ans1:
        saa = s - aa
        left = bisect_left(ans2, saa)
        right = bisect_right(ans2, saa)
        ans += right - left

    print(ans)


if __name__ == "__main__":
    main()
