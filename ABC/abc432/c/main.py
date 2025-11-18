import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    D = y - x  # > 0

    # すべての i で Ai*X ≡ W (mod D) が成り立つ必要がある。
    # よって (Ai*X) % D は全 i で等しくなければ不可能。
    r0 = (a[0] * x) % D

    # 区間 [Li, Ri] の共通部分に k が存在するかチェックし、最大の k を選ぶ。
    # Li = floor(Ai*X / D), Ri = Li + Ai
    L_max = -1
    R_min = 10**30
    sum_L = 0

    for Ai in a:
        if (Ai * x) % D != r0:
            print(-1)
            return
        Li = (Ai * x) // D
        Ri = Li + Ai
        if Li > L_max:
            L_max = Li
        if Ri < R_min:
            R_min = Ri
        sum_L += Li

    if L_max > R_min:
        print(-1)
        return

    # 最大化のため k は R_min を選ぶ
    k = R_min
    total_big = n * k - sum_L
    print(total_big)


if __name__ == "__main__":
    main()
