import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():return sys.stdin.readline().rstrip()



def main():
    import math
    n = int(input())
    a = sorted(set(map(int, input().split())))

    
    print(2*min(a))
    

if __name__ == '__main__':
    main()
