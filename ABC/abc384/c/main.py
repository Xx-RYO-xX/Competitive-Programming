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
    a, b, c, d, e = map(int, input().split())
    
    mondai = {"A":a, "B":b, "C":c, "D":d, "E":e}
    
    name = bit_full_search(["A", "B", "C", "D", "E"], 5)[1:]
    
    ans = dict()
    for NAME in name:
        score = 0
        for chr in NAME:
            score += mondai[chr]
        ans["".join(NAME)] = score
    
    ans = sorted(ans.items(), key=lambda x: (-x[1], x[0]))
    for name, score in ans:
        print(name)

if __name__ == '__main__':
    main()
