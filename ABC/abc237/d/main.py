import sys


def input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self, value):
        self.value = value
        self.nex = None
        self.prev = None


def main():
    n = int(input())
    s = input()
    a = {0: Node(0)}
    hasi = 0
    for i in range(1, n + 1):
        a[i] = Node(i)
        if s[i - 1] == "L":
            left = a[i - 1].prev
            if left == None:
                a[i - 1].prev = a[i]
                a[i].nex = a[i - 1]
            else:
                a[i - 1].prev = a[i]
                a[i].nex = a[i - 1]
                left.nex = a[i]
                a[i].prev = left

            if hasi == i - 1:
                hasi = i
        else:
            right = a[i - 1].nex
            if right == None:
                a[i - 1].nex = a[i]
                a[i].prev = a[i - 1]
            else:
                a[i - 1].nex = a[i]
                a[i].prev = a[i - 1]
                right.prev = a[i]
                a[i].nex = right

    while True:
        print(hasi, end=" ")
        nex = a[hasi].nex
        if nex == None:
            break
        hasi = nex.value


if __name__ == "__main__":
    main()
