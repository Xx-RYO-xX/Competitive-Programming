import sys 


def input():return sys.stdin.readline().rstrip()


def is_between_cyclic(a, b, c, n):
    """円周上で、点cが点aと点bの間にあるかを判定（時計回り）"""
    if a < b:
        return a < c < b
    else:  # 円周をまたぐ場合
        return c > a or c < b


def is_crossing(a, b, c, d, n):
    """線分(a,b)と線分(c,d)が交差するかを判定"""
    # 同じ点を共有する場合は交わらない
    if a == c or a == d or b == c or b == d:
        return False
    
    # 円周上で点a,b,c,dが交互に現れるかを判定
    # 時計回りに見て、点cが弧a→bにあり、点dが弧b→aにある、またはその逆
    return (is_between_cyclic(a, b, c, n) and is_between_cyclic(b, a, d, n)) or \
           (is_between_cyclic(a, b, d, n) and is_between_cyclic(b, a, c, n))


def main():
    # アンダースコア区切りの入力を処理
    n, m = map(int, input().split())
    lines = []
    for _ in range(m):
        a, b = map(int, input().split())
        lines.append((a, b))
    
    count = 0
    for i in range(m):
        a, b = lines[i]
        for j in range(i + 1, m):
            c, d = lines[j]
            if is_crossing(a, b, c, d, n):
                count += 1
    
    print(count)


if __name__ == '__main__':
    sys.exit(main())
