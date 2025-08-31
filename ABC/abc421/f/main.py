import sys


def input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self, value):
        self.value = value
        self.nex = None
        self.prev = None


def main():
    q = int(input())

    value_node = {0: Node(0)}

    for i in range(1, q + 1):
        query = input()

        if query[0] == "1":
            num, x = map(int, query.split())
            x_node = value_node[x]

            i_node = Node(i)
            value_node[i] = i_node

            before_nex = x_node.nex
            x_node.nex = i_node
            i_node.prev = x_node
            i_node.nex = before_nex

            if before_nex:
                before_nex.prev = i_node
        else:
            num, x, y = map(int, query.split())

            x_node = value_node[x]
            y_node = value_node[y]

            start_node1, end_node1 = x_node, y_node
            start_node2, end_node2 = y_node, x_node

            ans = 0
            ans1 = 0
            ans2 = 0
            now_node1 = start_node1.nex
            now_node2 = start_node2.nex
            while True:
                if now_node1 == end_node1:
                    start_node1.nex = end_node1
                    end_node1.prev = start_node1
                    ans = ans1
                    break
                if now_node2 == end_node2:
                    start_node2.nex = end_node2
                    end_node2.prev = start_node2
                    ans = ans2
                    break

                try:
                    ans1 += now_node1.value
                    now_node1 = now_node1.nex
                except:
                    None

                try:
                    ans2 += now_node2.value
                    now_node2 = now_node2.nex
                except:
                    None

            print(ans)


if __name__ == "__main__":
    main()
