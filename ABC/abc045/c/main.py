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
    s = input()

    ans = 0
    for idx in bit_full_search(range(len(s)-1), len(s)-1):
        siki = ""
        for i in range(len(s)):
            siki += s[i]
            if i in idx:
                siki += "+"
        
        ans += eval(siki)
    
    print(ans)

if __name__ == '__main__':
    sys.exit(main())
