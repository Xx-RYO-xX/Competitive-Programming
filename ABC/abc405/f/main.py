import sys


def input(): return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    total_points = 2*n

    # 各線分を「区間」として表現するための前処理
    segments = []
    for _ in range(m):
        a, b = map(int, input().split())
        # 必ず a < b となるように調整
        if a > b:
            a, b = b, a
        segments.append((a, b))

    # 交差判定の高速化のための前処理
    # 各点iを通る線分のインデックスを記録
    point_to_segments = [[] for _ in range(total_points + 1)]
    for i, (a, b) in enumerate(segments):
        point_to_segments[a].append(i)
        point_to_segments[b].append(i)

    # 各クエリを処理
    q = int(input())
    for _ in range(q):
        c, d = map(int, input().split())
        
        # 必ず c < d となるように調整
        if c > d:
            c, d = d, c
            
        result = 0
        
        # 線分cd が偶数点を通るかチェック
        points_between = set()
        
        # cからdまでの間の点を集める（円周をまたがない場合）
        if c < d:
            for i in range(c+1, d):
                if i % 2 == 0:  # 偶数点のみ考慮
                    points_between.add(i)
        # cからdまでの間の点を集める（円周をまたぐ場合）
        else:
            for i in range(c+1, total_points + 1):
                if i % 2 == 0:
                    points_between.add(i)
            for i in range(1, d):
                if i % 2 == 0:
                    points_between.add(i)
        
        # 交差判定
        checked_segments = set()
        for point in points_between:
            for seg_idx in point_to_segments[point]:
                if seg_idx not in checked_segments:
                    a, b = segments[seg_idx]
                    
                    # 線分abと線分cdが交差するかを判定
                    # 交差条件：円周上で点が交互に現れる
                    if (c < a < d < b) or (a < c < b < d) or \
                       (c < b < d < a) or (b < c < a < d):
                        result += 1
                    
                    checked_segments.add(seg_idx)
        
        print(result)


if __name__ == '__main__':
    sys.exit(main())
