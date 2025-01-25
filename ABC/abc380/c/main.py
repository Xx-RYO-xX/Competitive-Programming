from itertools import groupby
import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():
    return sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    s = input()
    
    blocks = []
    i = 0
    while i < n:
        if s[i] == '1':
            start = i
            while i < n and s[i] == '1':
                i += 1
            end = i
            blocks.append((start, end))
        else:
            i += 1
    

    block_k_1 = blocks[k-2]
    block_k = blocks[k-1]
    
    ans = []

    ans.append(s[:block_k_1[1]])
    ans.append(s[block_k[0]:block_k[1]])
    ans.append(s[block_k_1[1]:block_k[0]])
    ans.append(s[block_k[1]:])
    
    print(''.join(ans))

if __name__ == '__main__':
    main()
