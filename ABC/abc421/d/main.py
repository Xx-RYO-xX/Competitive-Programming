import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    rt, ct, ra, ca = map(int, input().split())
    n, m, l = map(int, input().split())
    s = deque()
    for _ in range(m):
        st, at = input().split()
        s.append([st, int(at)])

    t = deque()
    for _ in range(l):
        tt, bt = input().split()
        t.append([tt, int(bt)])

    # print(s)
    # print(t)

    s_same, t_same = [], []
    while s or t:
        ss, aa = s.popleft()
        tt, bb = t.popleft()

        if aa > bb:
            s.appendleft([ss, aa - bb])
            s_same.append([ss, bb])
            t_same.append([tt, bb])
        elif aa < bb:
            t.appendleft([tt, bb - aa])
            s_same.append([ss, aa])
            t_same.append([tt, aa])
        else:
            s_same.append([ss, aa])
            t_same.append([tt, bb])

    # print(s_same)
    # print(t_same)

    direction = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
        "UL": (-1, -1),
        "UR": (1, -1),
        "DL": (-1, 1),
        "DR": (1, 1),
    }

    ans = 0
    for i in range(len(s_same)):
        sm, am = s_same[i]
        tm, bm = t_same[i]

        dr_t, dc_t = direction[sm]
        dr_a, dc_a = direction[tm]

        if sm == tm:
            if rt == ra and ct == ca:
                ans += am

        else:
            dr_sa = dr_t - dr_a
            r_sa = ra - rt

            dc_sa = dc_t - dc_a
            c_sa = ca - ct

            kr = None
            kc = None

            if dr_sa != 0:
                if r_sa % dr_sa == 0:
                    kr = r_sa // dr_sa
            elif r_sa != 0:
                rt += dr_t * am
                ct += dc_t * am
                ra += dr_a * bm
                ca += dc_a * bm
                continue

            if dc_sa != 0:
                if c_sa % dc_sa == 0:
                    kc = c_sa // dc_sa
            elif c_sa != 0:
                rt += dr_t * am
                ct += dc_t * am
                ra += dr_a * bm
                ca += dc_a * bm
                continue

            k = 0
            if not (kr == None and kc == None):
                if kr == kc:
                    k = kr
                elif kr == None:
                    k = kc
                elif kc == None:
                    k = kr

            if 1 <= k <= am:
                ans += 1

        rt += dr_t * am
        ct += dc_t * am

        ra += dr_a * bm
        ca += dc_a * bm

    print(ans)


if __name__ == "__main__":
    main()
