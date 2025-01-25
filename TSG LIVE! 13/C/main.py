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
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(input()))
    
    w_lst = bit_full_search(range(w), w)[1:]
    
    # print(w_lst)
    
    ans = 0
    aa = a[:]
    # print(aa)
    for W in w_lst:
        print(*aa, sep="\n")
        # print(W)
        for ww in W:
            for i in range(h):
                aa[i][ww] = "x"
        
        for y in range(h):
            o_count = 0
            for x in range(w):
                if aa[y][x] == "o":
                    o_count += 1
                if 1 < o_count:
                    break
            else:
                continue
            break
        else:
            ans += 1
        aa = []
        aa = a[:]
    
    print(ans)

if __name__ == '__main__':
    main()