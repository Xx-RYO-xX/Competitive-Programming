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
        ans.append(s_u_m)

    return ans


def main():
    n, m = map(int, input().split())
    edge = []
    for _ in range(m):
        u, v = map(int, input().split())
        edge.append((u, v))

    ans = m

    for group in bit_full_search(range(n), n):
        anst = 0
        for u, v in edge:
            if (u in group and v in group) or (u not in group and v not in group):
                anst += 1

        ans = min(ans, anst)

    print(ans)


if __name__ == "__main__":
    main()
