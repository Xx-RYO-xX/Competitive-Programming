import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():return sys.stdin.readline().rstrip()


def main():
    abcde = []
    for i in range(5):
        abcde.append(int(input()))
    k = int(input())
    # print(abcde)
    for i in range(5):
        for j in range(i+1, 5):
            if k < abs(abcde[j] - abcde[i]):
                print(":(")
                exit()

    print("Yay!")

if __name__ == '__main__':
    main()
