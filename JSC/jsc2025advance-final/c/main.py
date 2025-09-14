import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    for _ in range(int(input())):
        na, nb, nc = map(int, input().split())
        ac_cnt = min(na, nc)
        moji = na + nb + nc
        if moji - (ac_cnt * 2) >= ac_cnt:
            print(ac_cnt)
        else:
            tac = nb + max(na, nc) - min(na, nc)
            print(tac + ((ac_cnt - tac) // 2))


if __name__ == "__main__":
    main()
