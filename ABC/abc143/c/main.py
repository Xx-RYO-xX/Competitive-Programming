import sys 


def input():return sys.stdin.readline().rstrip()


def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    from itertools import groupby
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res



def main():
    n = int(input())
    s = input()
    
    print(len(runLengthEncode(S=s)))


if __name__ == '__main__':
    sys.exit(main())
