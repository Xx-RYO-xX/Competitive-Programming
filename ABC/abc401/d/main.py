import sys

def input():return sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    s = list(input())
    
    # 前向きDP（単一テーブル）
    dp = [[[False for _ in range(2)] for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0][0] = True
    
    # 前向きDP計算
    for i in range(n):
        for j in range(k+1):
            for p in range(2):
                if not dp[i][j][p]: continue
                if s[i] in ['.', '?']: dp[i+1][j][0] = True
                if s[i] in ['o', '?'] and p == 0 and j < k: dp[i+1][j+1][1] = True
    
    # 後ろからの情報 (同じサイズのテーブルだが、DP計算は別途実行)
    back = [[[False for _ in range(2)] for _ in range(k+1)] for _ in range(n+1)]
    back[n][0][0] = True
    
    # 後ろ向き計算
    for i in range(n-1, -1, -1):
        for j in range(k+1):
            for p in range(2):
                if not back[i+1][j][p]: continue
                if s[i] in ['.', '?']: back[i][j][0] = True
                if s[i] in ['o', '?'] and p == 0 and j < k: back[i][j+1][1] = True
    
    # 結果生成
    result = []
    for i in range(n):
        dot_ok = o_ok = False
        
        # ドット配置可能判定
        if s[i] in ['.', '?']:
            for j1 in range(k+1):
                for p in range(2):
                    if dp[i][j1][p] and j1 <= k and any(back[i+1][k-j1][x] for x in range(2)):
                        dot_ok = True
                        break
                if dot_ok: break
        
        # o配置可能判定
        if s[i] in ['o', '?']:
            for j1 in range(k):
                if dp[i][j1][0] and k-j1-1 >= 0 and back[i+1][k-j1-1][0]:
                    o_ok = True
                    break
        
        result.append('?' if dot_ok and o_ok else 'o' if o_ok else '.')
    
    print(''.join(result))

if __name__ == '__main__':
    sys.exit(main())
