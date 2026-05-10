import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    h, w = map(int, input().split())
    n = int(input())
    door = defaultdict(list)
    for _ in range(n):
        a, b = map(int, input().split())
        door[a].append(b)

    ansa = 0
    ansb = 0
    ouhuku = 0
    modoru = []
    tooru = []
    for i in door:
        b = sorted(door[i])

        ansa += 2 * (b[-1] - 1)

        modo_cost_min = min(2 * (b[-1] - 1), 2 * (w - b[0]))
        for j in range(len(b) - 1):
            modo_cost_min = min(modo_cost_min, 2 * (b[j] - 1) + 2 * (w - b[j + 1]))

        if w - 1 < modo_cost_min:
            ansb += w - 1
            ouhuku += 1
            tooru.append(modo_cost_min - (w - 1))
        else:
            ansb += modo_cost_min
            modoru.append(w - 1 - modo_cost_min)

    modoru.append(w - 1)
    modoru.append(w - 1)
    modoru.sort()
    tooru.sort()
    # print(modoru)
    # print(tooru)

    if ouhuku == 0:
        ansb += modoru[0] + modoru[1]
    elif ouhuku == 1:
        ansb += modoru[0]
    elif ouhuku % 2 != 0:
        ansb += min(
            modoru[0] if modoru else float("inf"), tooru[0] if tooru else float("inf")
        )

    # print(ansa, ansb)
    print(min(ansa, ansb))


if __name__ == "__main__":
    main()
