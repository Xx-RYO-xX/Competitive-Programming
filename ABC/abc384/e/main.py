import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def main():
    # 入力: グリッドサイズとXの値
    h, w, x = map(int, input().split())
    
    # 入力: 高橋くんの初期位置（1-indexed → 0-indexed）
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    
    # 入力: スライムの強さグリッド
    s = [list(map(int, input().split())) for _ in range(h)]
    
    # 高橋くんの初期の強さを取得
    power = s[p][q]
    s[p][q] = 0  # 初期位置を吸収済み（0 にする）
    
    # BFSの初期化
    queue = deque([(p, q)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右への移動
    
    # BFSを実行して体を広げる
    while queue:
        i, j = queue.popleft()
        
        # 隣接マスを探索
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            # 範囲外チェックと未吸収チェック
            if 0 <= ni < h and 0 <= nj < w and s[ni][nj] > 0:
                # 吸収条件を満たす場合のみ処理
                if s[ni][nj] < power * x:
                    power += s[ni][nj]  # スライムを吸収
                    s[ni][nj] = 0       # 吸収済みとして0にする
                    queue.append((ni, nj))  # 次の探索対象として追加
    
    # 結果を出力
    print(power)

if __name__ == '__main__':
    main()
