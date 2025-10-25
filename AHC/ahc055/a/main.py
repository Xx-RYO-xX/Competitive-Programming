import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    h = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    # 現在の宝箱の硬さ
    health = h[:]
    # 武器の耐久値
    durability = c[:]
    # 利用可能な武器（宝箱が開いたか）
    available = [False] * n

    attacks = []

    # すべての宝箱を開くまで攻撃を続ける
    while any(health[i] > 0 for i in range(n)):
        # 次の攻撃を選ぶ
        best_weapon = -1
        best_box = -1
        best_efficiency = 0

        # 素手での攻撃を検討
        for box in range(n):
            if health[box] > 0:
                # 素手でこの宝箱を攻撃するのは常に効率1
                best_box = box
                best_weapon = -1
                best_efficiency = 1
                break

        # 利用可能な武器での攻撃を検討
        for weapon in range(n):
            if available[weapon] and durability[weapon] > 0:
                for box in range(n):
                    if health[box] > 0:
                        damage = a[weapon][box]
                        # 効率 = min(ダメージ, 残りHP)
                        efficiency = min(damage, health[box])
                        if efficiency > best_efficiency:
                            best_weapon = weapon
                            best_box = box
                            best_efficiency = efficiency

        # 攻撃を実行
        attacks.append((best_weapon, best_box))

        if best_weapon == -1:
            # 素手攻撃
            health[best_box] -= 1
        else:
            # 武器攻撃
            health[best_box] -= a[best_weapon][best_box]
            durability[best_weapon] -= 1

        # 宝箱が開いたかチェック
        if health[best_box] <= 0 and not available[best_box]:
            available[best_box] = True

    # 結果を出力
    for weapon, box in attacks:
        print(weapon, box)


if __name__ == "__main__":
    main()
