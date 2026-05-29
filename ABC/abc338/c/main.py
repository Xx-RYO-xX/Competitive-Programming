import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from pulp import LpMinimize, LpMaximize, LpProblem, LpVariable, value, PULP_CBC_CMD

    n = int(input())
    q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    prob = LpProblem(sense=LpMaximize)
    acnt = LpVariable("acnt", lowBound=0, cat="Integer")
    bcnt = LpVariable("bcnt", lowBound=0, cat="Integer")
    prob += acnt + bcnt
    for i in range(n):
        prob += a[i] * acnt + b[i] * bcnt <= q[i]

    prob.solve(PULP_CBC_CMD(msg=False))

    print(int(value(acnt) + value(bcnt)))


if __name__ == "__main__":
    main()
