import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():return sys.stdin.readline().rstrip()


def main():
    n = input()
    if n.count("1") == 1 and n.count("2") == 2 and n.count("3") == 3:
        print("Yes")
    else:
        print("No")
        

if __name__ == '__main__':
    main()
