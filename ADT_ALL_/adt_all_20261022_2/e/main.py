import math

def euclid_distace(x1, y1, x2, y2):
    """
    ユークリッド距離を求める関数だっピ\n
    ￣￣V￣￣￣￣￣￣￣￣￣￣￣￣￣￣\n
    ( ・3・)\n
    /｜｜｜\\
    
    Parameters
    ----------
    x1 : int
        1点目のx座標
    y1 : int
        1点目のy座標
    x2 : int
        2点目のx座標
    y2 : int
        2点目のy座標
        
    Returns
    -------
    return : float
        2点間のユークリッド距離
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)



def main():
    import sys

    input = sys.stdin.readline
    n, d = map(int, input().split())
    ans = [False]*n
    ans[0]= True
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((_, x, y))
    
    for _ in range(10):
        for i in range(n):
            ii, x1, y1 = xy[i]
            for j in range(n):
                jj, x2, y2 = xy[j]
                if any([ans[ii], ans[jj]]) and (x1-x2)**2 + (y1- y2)**2  <= d**2:
                    ans[ii] = True
                    ans[jj] = True

    for ANS in ans:
        print("Yes" if ANS else "No")

if __name__ == "__main__":
    main()
