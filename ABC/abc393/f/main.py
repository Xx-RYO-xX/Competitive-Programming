import sys


def input(): return sys.stdin.readline().rstrip()


def find_longest_increasing_subsequence(arr, r, x):
    # x以下の要素のみを取り出す
    filtered = [(v, i) for i, v in enumerate(arr[:r]) if v <= x]
    if not filtered:
        return 0
    
    # LISを求める
    n = len(filtered)
    dp = [float('inf')] * (n + 1)
    dp[0] = -float('inf')
    
    for v, _ in filtered:
        # 二分探索でvを挿入できる位置を探す
        left, right = 0, n
        while left < right:
            mid = (left + right + 1) // 2
            if dp[mid] < v:
                left = mid
            else:
                right = mid - 1
        dp[left + 1] = min(dp[left + 1], v)
    
    # LISの長さを返す
    for i in range(n, -1, -1):
        if dp[i] != float('inf'):
            return i
    return 0


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    for _ in range(q):
        r, x = map(int, input().split())
        result = find_longest_increasing_subsequence(a, r, x)
        print(result)


if __name__ == '__main__':
    sys.exit(main())