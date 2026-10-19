def main():
    import sys

    from collections import deque

    input = sys.stdin.readline
    n, m, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    # print(a)
    hito_to_basho = [-1] * (n + 1)
    instance = []
    for _ in range(m + 1):
        instance.append([0, deque([]), dict()])
    # print(instance)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que, x, y = query
            if hito_to_basho[x] != -1:
                p = hito_to_basho[x][1]
                match hito_to_basho[x][0]:
                    case 1:
                        instance[p][0] -= 1
                        while instance[p][1] and instance[p][2]:
                            poped1 = instance[p][1].popleft()
                            if poped1 in instance[p][2] and instance[p][2][poped1] > 0:
                                instance[p][2][poped1] -= 1
                            else:
                                instance[p][1].appendleft(poped1)
                                break
                        if instance[p][1]:
                            poped = instance[p][1].popleft()
                            hito_to_basho[poped] = [1, p]
                            instance[p][0] += 1
                    case 2:
                        if x in instance[p][2]:
                            instance[p][2][x] += 1
                        else:
                            instance[p][2][x] = 1

            if instance[y][0] < a[y]:
                instance[y][0] += 1
                hito_to_basho[x] = [1, y]
            else:
                instance[y][1].append(x)
                hito_to_basho[x] = [2, y]

        else:
            que, z = query
            if hito_to_basho[z] != -1:
                print(*hito_to_basho[z])
            else:
                print(-1)


if __name__ == "__main__":
    main()
