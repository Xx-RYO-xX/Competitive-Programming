import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    def bfs(start):
        from collections import deque

        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        while q:
            pos = q.popleft()
            for nex in g[pos]:
                if dist[nex] == -1:
                    dist[nex] = dist[pos] + 1
                    q.append(nex)
        return dist

    start = bfs(1)
    start_dist = max(start)

    hasi1_node = 0
    for i in range(1, n + 1):
        if start[i] == start_dist:
            hasi1_node = max(hasi1_node, i)

    hasi_to_hasi1 = bfs(hasi1_node)
    hasi1_dist = max(hasi_to_hasi1)

    hasi2_node = 0
    for i in range(1, n + 1):
        if hasi_to_hasi1[i] == hasi1_dist:
            hasi2_node = max(hasi2_node, i)

    hasi_to_hasi2 = bfs(hasi2_node)

    for i in range(1, n + 1):
        anst1 = hasi_to_hasi1[i]
        anst2 = hasi_to_hasi2[i]

        if anst1 > anst2:
            print(hasi1_node, end="\n")
        elif anst1 < anst2:
            print(hasi2_node, end="\n")
        else:
            print(max(hasi1_node, hasi2_node), end="\n")


if __name__ == "__main__":
    main()
