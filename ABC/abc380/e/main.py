from collections import defaultdict
import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():return sys.stdin.readline().rstrip()



def main():
    n, q = map(int, input().split())
    c = [1]*n
    for _ in range(q):
        query = input()
        if query[0] == "1":
            x, c = int(query[2])-1, int(query[-1])-1
        else:            
            c = int(query[-1])-1
            


if __name__ == '__main__':
    main()
