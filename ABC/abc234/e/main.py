import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from pulp import LpMinimize, LpProblem, LpVariable, value, PULP_CBC_CMD

    x = int(input())

    ans = []

    for i in range(len(str(x)), len(str(x)) + 2):
        prob = LpProblem(sense=LpMinimize)
        d0 = LpVariable("d0", lowBound=1, upBound=9, cat="Integer")
        diff = LpVariable("diff", lowBound=-9, upBound=9, cat="Integer")
        for k in range(i):
            prob += d0 + k * diff >= 0
            prob += d0 + k * diff <= 9
        n = sum((d0 + k * diff) * (10 ** (i - 1 - k)) for k in range(i))
        prob += n >= x
        prob += n
        prob.solve(PULP_CBC_CMD(msg=False))
        val = value(n)
        if val is not None:
            ans.append(int(val))
            break
    print(min(ans))


if __name__ == "__main__":
    main()
