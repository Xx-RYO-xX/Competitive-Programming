import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import bisect
    from collections import defaultdict

    n, m = map(int, input().split())
    l_to_r = [[] for _ in range(n + 1)]
    r_to_l = [[] for _ in range(n + 1)]

    lr = defaultdict(int)
    for _ in range(m):
        l, r = map(int, input().split())
        l_to_r[l].append(r)
        r_to_l[r].append(l)
        lr[(l, r)] += 1

    for i in range(n + 1):
        l_to_r[i].sort()
        r_to_l[i].sort()

    l_i_min = [float("inf")] * (n + 2)
    for i in range(n, -1, -1):
        l_i_min[i] = l_i_min[i + 1]
        if l_to_r[i]:
            l_i_min[i] = min(l_i_min[i], l_to_r[i][0])

    r_i_max = [-float("inf")] * (n + 2)
    for i in range(1, n + 1):
        r_i_max[i] = r_i_max[i - 1]
        if r_to_l[i]:
            r_i_max[i] = max(r_i_max[i], r_to_l[i][-1])

    q = int(input())
    # print(l_to_r)
    # print(r_to_l)
    for _ in range(q):
        s, t = map(int, input().split())
        if not l_to_r[s] or not r_to_l[t]:
            print("No")
            continue

        s_hasi_idx = bisect.bisect_right(l_to_r[s], t)
        if not s_hasi_idx:
            print("No")
            continue
        s_hasi = l_to_r[s][s_hasi_idx - 1]

        t_hasi_idx = bisect.bisect_left(r_to_l[t], s)
        if len(r_to_l[t]) == t_hasi_idx:
            print("No")
            continue
        t_hasi = r_to_l[t][t_hasi_idx]

        if (s, s_hasi) == (t_hasi, t):
            if lr[(s, s_hasi)] > 1:
                print("Yes")
                continue

            if l_i_min[s] < t:
                print("Yes")
                continue

            if s < r_i_max[t]:
                print("Yes")
                continue

            print("No")
            continue
        # print(s, s_hasi)
        # print(t_hasi, t)
        print("Yes" if t_hasi <= s_hasi + 1 else "No")


if __name__ == "__main__":
    main()
