import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import groupby
    n = int(input())
    s = input()
    def runLengthEncode(S: str) -> "List[tuple(str, int)]":
        grouped = groupby(S)
        res = []
        for k, v in grouped:
            res.append((k, int(len(list(v)))))
        return res
    
    s = runLengthEncode(S=s)
    print(s)
    stack = [[]]*2
    start = set(["B", "K"])
    for i in range(len(s)):
        if s[i] 

if __name__ == '__main__':
    main()
