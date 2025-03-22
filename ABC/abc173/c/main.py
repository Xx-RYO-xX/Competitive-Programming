import sys


def input():return sys.stdin.readline().rstrip()


def bit_full_search(lst, n):
    """
    ビット全探索する関数

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
    for i in range(2 ** n):
        s_u_m = []
        for j in range(n):
            bit = (2 ** j)
            if (i // bit) % 2 == 1:
                s_u_m.append(lst[j])
        ans.append(s_u_m)

    return ans




def main():
    from copy import deepcopy
    from collections import Counter
    h, w, k = map(int, input().split())
    c = []
    for _ in range(h):
        c.append(list(input()))
        
    # print(c)
    
    ans = 0
    for h_bit in bit_full_search(list(range(h)), h):
        # print(h_bit)
        for w_bit in bit_full_search(list(range(w)), w):
            # print(w_bit)
            cc = deepcopy(c)
            for hh in range(h):
                for ww in range(w):
                    if hh in h_bit or ww in w_bit:
                        cc[hh][ww] = "red"
            count_b = 0
            for hh in range(h):
                count_b += Counter(cc[hh])["#"]
            if count_b == k: ans += 1
    print(ans)

if __name__ == '__main__':
    main()
