import sys


def input():
    return sys.stdin.readline().rstrip()


def my_sign(x):
    return (x > 0) - (x < 0)


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
    n = int(input())
    l = list(map(int, input().split()))

    ans = 0
    for i in range(2**n):
        pos = 0.5
        anst = 0
        for j in range(n):
            bit = 2**j
            bpos = pos
            if (i // bit) % 2 == 1:
                pos += l[j]
            else:
                pos -= l[j]
            if my_sign(pos) != my_sign(bpos):
                anst += 1
        ans = max(ans, anst)

    print(ans)


if __name__ == "__main__":
    main()
