import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():return sys.stdin.readline().rstrip()


def main():
    import heapq
    n = int(input())
    a = list(map(int, input().split()))
    
    heapq.heapify(a)
    print(a)

if __name__ == '__main__':
    main()
