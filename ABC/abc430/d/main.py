import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    n = int(input())
    x = list(map(int, input().split()))

    suuchokusenn = SortedList([0])

    def d(i):
        res = []
        if 0 < i:
            res.append(abs(suuchokusenn[i - 1] - suuchokusenn[i]))
        if i < len(suuchokusenn) - 1:
            res.append(abs(suuchokusenn[i] - suuchokusenn[i + 1]))
        return min(res) if len(res) > 0 else 0

    ans = 0
    for X in x:
        idx = suuchokusenn.bisect(X)
        print(X, idx)
        zengo = [idx - 1, idx + 1]
        for ii in zengo:
            if 0 < ii < len(suuchokusenn):
                print(ii, d(ii))
                ans -= d(ii)

        suuchokusenn.add(X)
        zengo = [idx - 1, idx + 1]
        for ii in zengo:
            if 0 < ii < len(suuchokusenn):
                print(ii, d(ii))
                ans += d(ii)

        # print(ans)


if __name__ == "__main__":
    main()
