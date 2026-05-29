import sys
import numpy as np


def input():
    return sys.stdin.readline().rstrip()


## https://qiita.com/hacchi_/items/7e6f433d465df9378d7a
def sankaku(abc):
    for i in range(3):
        a = abc[(0 + i) % 3]
        b = abc[(1 + i) % 3]
        c = abc[(2 + i) % 3]
        # ベクトルを定義
        vec_a = a - b
        vec_c = c - b

        # コサインの計算
        length_vec_a = np.linalg.norm(vec_a)
        length_vec_c = np.linalg.norm(vec_c)
        inner_product = np.inner(vec_a, vec_c)
        cos = inner_product / (length_vec_a * length_vec_c)

        # 角度（ラジアン）の計算
        rad = np.arccos(cos)

        # 弧度法から度数法（rad ➔ 度）への変換
        degree = np.rad2deg(rad)
        if degree == 90:
            return 1
        if degree > 90:
            return 2
    return 0


def main():
    from itertools import combinations

    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append(np.array([x, y]))

    ans = [0, 0, 0]
    for comb in combinations(xy, 3):
        ans[sankaku(comb)] += 1

    for i in range(3):
        print(ans[i], sep=" ")
    print()


if __name__ == "__main__":
    main()
