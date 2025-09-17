import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from pulp import LpMaximize, LpProblem, LpVariable, value, PULP_CBC_CMD

    x, c = map(int, input().split())

    prob = LpProblem(sense=LpMaximize)

    i = LpVariable("ans", cat="Integer")
    ans = 1000 * i
    prob += ans + (ans * (c / 1000)) <= x
    prob.solve(PULP_CBC_CMD(msg=False))

    print(int(value(ans)))


if __name__ == "__main__":
    main()
