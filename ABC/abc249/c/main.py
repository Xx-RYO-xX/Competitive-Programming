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
    from collections import Counter
    n, k = map(int, input().split())
    s = [] 
    for _ in range(n):
        s.append(input())
    
    idx_lst = bit_full_search(range(n), n)
    
    ans = 0
    for idx in idx_lst:
        count = dict()
        for i in idx:
            count = Counter(count) + Counter(s[i])
        
        sum = 0
        for C in count:
            if count[C] == k:
                sum += 1
        ans = max(ans, sum)
    
    print(ans)

if __name__ == '__main__':
    sys.exit(main())
