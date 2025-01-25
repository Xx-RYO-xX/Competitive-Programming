import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, x, y = map(int, input().split())
    ax = []
    by = []
    for _ in range(n):
        at, bt = map(int, input().split())
        ax.append(at)
        by.append(bt)

    t_min, t_max = 0, 10**10
    for i in range(n):
        diff = y - by[i]
        if diff == 0:
            if x > ax[i]:
                print("No")
                return
        elif diff > 0:
            limit = (ax[i] - x) // diff
            if (ax[i] - x) < 0 and (ax[i] - x) % diff != 0:
                limit -= 1
            t_max = min(t_max, limit)
        else:
            diff = (by[i] - y)
            limit = (x - ax[i] + diff - 1) // diff
            t_min = max(t_min, limit)
        if t_min > t_max:
            print("No")
            return

    print("Yes")
    


if __name__ == '__main__':
    sys.exit(main())
