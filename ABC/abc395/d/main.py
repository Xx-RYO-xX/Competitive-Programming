import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    
    hato_su = [i for i in range(n+1)]
    su_hato = hato_su.copy()
    su_hato_inv = hato_su.copy()

    for _ in range(q):
        op = input()
        if op[0] == "1":
            t, a, b = map(int, op.split())
            hato_su[a] = su_hato_inv[b]
        elif op[0] == "2":
            t, a, b = map(int, op.split())
            ta = su_hato_inv[a]
            tb = su_hato_inv[b]
            su_hato[ta], su_hato[tb] = su_hato[tb], su_hato[ta]
            su_hato_inv[a], su_hato_inv[b] = tb, ta

        else:
            t, a = map(int, op.split())
            print(su_hato[hato_su[a]])


if __name__ == '__main__':
    sys.exit(main())
