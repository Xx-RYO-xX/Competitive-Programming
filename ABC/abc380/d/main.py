import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():return sys.stdin.readline().rstrip()


def main():
    s = input().strip()
    q = int(input())
    k = list(map(int, input().split()))
    len_s = len(s)
    ans = []
    for K in k:
        pos = len_s
        swap = 0
        while pos < K:
            pos *= 2
        while pos > len_s:
            if K <= pos // 2:
                pos //= 2
            else:
                K -= pos // 2
                pos //= 2
                swap ^= 1
        c = s[K - 1]
        if swap % 2 == 1:
            c = c.swapcase()
        ans.append(c)
    print(*ans, sep=" ")

if __name__ == '__main__':
    main()
