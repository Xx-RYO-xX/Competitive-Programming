import sys


def input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self, value):
        self.value = value
        self.nex = None
        self.prev = None


def main():
    from collections import defaultdict

    n, q = map(int, input().split())

    card = {1: Node(1)}
    bottom = set([1])
    for i in range(2, n + 1):
        card[i] = Node(i)
        bottom.add(i)

    for _ in range(q):
        c, p = map(int, input().split())
        if card[c].prev != None:
            card[c].prev.nex = None

        card[p].nex = card[c]
        card[c].prev = card[p]
        bottom.discard(c)

    ans = defaultdict(int)
    for b in bottom:
        anst = 1
        now = card[b]
        while now.nex != None:
            anst += 1
            now = now.nex
        ans[b] = anst

    for i in range(1, n + 1):
        print(ans[i], end=" ")


if __name__ == "__main__":
    main()
