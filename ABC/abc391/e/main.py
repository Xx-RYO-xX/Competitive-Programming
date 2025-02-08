import sys

def input():
    return sys.stdin.readline().rstrip()

def simulate_final(a_str):
    cur = list(a_str)
    while len(cur) > 1:
        nxt = []
        for i in range(0, len(cur), 3):
            triple = cur[i:i+3]
            # 多数決：0が2個以上なら0，そうでなければ1
            if triple.count('0') >= 2:
                nxt.append('0')
            else:
                nxt.append('1')
        cur = nxt
    return cur[0]

def main():
    n = int(input())
    a = input().strip()
    L = len(a)  # L = 3^n

    # 1. 元の最終結果をシミュレーション
    original_final = simulate_final(a)

    # 2. 葉レベルのDP初期化
    dp = []
    for ch in a:
        # 各葉は，chと一致する場合は0，一致しなければ1
        dp.append((0 if ch=='0' else 1, 0 if ch=='1' else 1))

    # 3. ボトムアップでDP構築
    # 各レベルで，dpの個数は1/3に減っていく．
    for _ in range(n):
        new_dp = []
        for i in range(0, len(dp), 3):
            left, mid, right = dp[i], dp[i+1], dp[i+2]
            # 候補 b=0 の場合のコスト
            cost0 = min(
                left[0] + mid[0] + right[0],
                left[0] + mid[0] + right[1],
                left[0] + mid[1] + right[0],
                left[1] + mid[0] + right[0]
            )
            # 候補 b=1 の場合のコスト
            cost1 = min(
                left[1] + mid[1] + right[1],
                left[1] + mid[1] + right[0],
                left[1] + mid[0] + right[1],
                left[0] + mid[1] + right[1]
            )
            new_dp.append((cost0, cost1))
        dp = new_dp

    # 4. 答えは元の最終結果と反対の値にする最小反転回数
    target = 1 - int(original_final)
    print(dp[0][target])

if __name__ == '__main__':
    sys.exit(main())
