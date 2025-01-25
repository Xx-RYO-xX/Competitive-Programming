from itertools import groupby
import sys


def input():return sys.stdin.readline().rstrip()


# def runLengthEncodeToString(S: str) -> str:
#     grouped = groupby(S)
#     res = ""
#     for k, v in grouped:
#         res += k + str(len(list(v)))
#     return res



def main():
    n = int(input())
    s = input()
    
    o_count = 0
    o_count_re = 0
    ans = 0
    for i in range(n):
        if s[i] == "o":
            o_count += 1
        else:
            ans = max(o_count, ans)
            o_count = 0
        
        if s[-1-i] == "o":
            o_count_re += 1
        else:
            ans = max(o_count_re, ans)
            o_count_re = 0
    
    print(-1 if ans == 0 else ans)



if __name__ == '__main__':
    main()
