import sys


class LinkedList:
    def __init__(self, prev, s):
        self.prev = prev
        self.s = s


def input():return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    sv = None
    pc = {str(i): None for i in range(1, n+1)}
    
    for _ in range(q):
        query = input()
        if query[0] == "1":
            num, p= query.split()
            pc[p] = sv
        elif query[0] == "2":
            num, p, s = query.split()
            pc[p] = LinkedList(pc[p], s)
        else:
            num, p = query.split()
            sv = pc[p]


    ans = []
    tsv = sv
    while tsv:
        ans.append(tsv.s)
        tsv = tsv.prev
    print("".join(reversed(ans)))


if __name__ == '__main__':
    main()
