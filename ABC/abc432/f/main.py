import sys


# def input():
#     return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) % n != 0:
        print(-1)
        return

    narasi = sum(a) // n

    if all(x == narasi for x in a):
        print(0)
        return

    goal = tuple([narasi] * n)

    q = deque([tuple(a)])
    visited = {tuple(a): None}

    while q:
        now_a = q.popleft()

        if now_a == goal:
            anst = []
            now = goal
            while visited[now] is not None:
                prev, xyz = visited[now]
                anst.append(xyz)
                now = tuple(prev)

            anst.reverse()
            print(len(anst))
            for ans in anst:
                print(ans[0] + 1, ans[1] + 1, ans[2])
            return

        now_a = list(now_a)

        for x in range(n):
            for y in range(n):
                if x == y:
                    continue

                if now_a[x] == 0:
                    continue

                zt = set()

                if now_a[y] < narasi:
                    ztt = narasi - now_a[y]
                    if 0 < ztt <= now_a[x]:
                        zt.add(ztt)

                if now_a[x] > narasi:
                    ztt = now_a[x] - narasi
                    if 0 < ztt <= now_a[x]:
                        zt.add(ztt)

                for z in zt:
                    nex_a = now_a[:]
                    nex_a[x] -= z
                    nex_a[y] += z
                    nex_a = tuple(nex_a)

                    if nex_a not in visited:
                        visited[nex_a] = (now_a, (x, y, z))
                        q.append(nex_a)


if __name__ == "__main__":
    main()
