import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()

    count = 0
    ans = []
    for i in range(1, len(s)):
        if s[i] == "-":
            count += 1
        else:
            ans.append(count)
            count = 0

    print(*ans, sep=" ")
    
if __name__ == '__main__':
    main()
