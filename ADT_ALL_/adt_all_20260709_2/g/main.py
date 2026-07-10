# 三分探索用のテンプレート作成
from math import sqrt

a, b = map(int, input().split())


# 関数計算用
def func(x):
    return a / sqrt(x + 1) + b * x  # ここに問題の関数を入力


left, right = 0, 10**18  # 定義域を入力(leftに小さい値を入力)
limit = 2  # 誤差の許容範囲を入力(求める値が整数値しか取らないときは2)

# 求める値の定義域が許容範囲内になるまで繰り返す
while abs(left - right) > limit:

    # 真ん中の値を計算
    mi1 = (2 * left + right) // 3
    mi2 = (left + 2 * right) // 3

    # 狭める方向を判定(条件式の不等号は適宜変更)
    if func(mi1) > func(mi2):
        left = mi1
    else:
        right = mi2

# 答えとなる値を出力(候補が複数ある場合は比較して出力)
ans = 10**18
for i in range(left, right + 1):
    ans = min(ans, func(i))

print(ans)
