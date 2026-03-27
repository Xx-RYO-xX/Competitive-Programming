import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    import heapq

    for _ in range(int(input())):
        n = int(input())
        x_to_y = defaultdict(set)
        y_to_x = defaultdict(set)
        for i in range(n):
            x, y = map(int, input().split())
            x_to_y[x].add(y)
            y_to_x[y].add(x)

        x_len = []
        for x in x_to_y:
            x_len.append([-len(x_to_y[x]), x])

        y_len = []
        for y in y_to_x:
            y_len.append([-len(y_to_x[y]), y])

        heapq.heapify(x_len)
        heapq.heapify(y_len)

        x_minus = defaultdict(int)
        y_minus = defaultdict(int)

        ans = 0
        while x_len and y_len:
            while True:
                xlen, x = heapq.heappop(x_len)
                if x_minus[x] == 0:
                    heapq.heappush(x_len, [xlen, x])
                    break
                heapq.heappush(x_len, [xlen + x_minus[x], x])
                x_minus[x] = 0
            while True:
                ylen, y = heapq.heappop(y_len)
                if y_minus[y] == 0:
                    heapq.heappush(y_len, [ylen, y])
                    break
                heapq.heappush(y_len, [ylen + y_minus[y], y])
                y_minus[y] = 0

            xlen, x = heapq.heappop(x_len)
            ylen, y = heapq.heappop(y_len)
            if xlen > ylen:
                z = x
                for yy in x_to_y.pop(z):
                    y_to_x[yy].discard(z)
                    y_minus[z] += 1
                    ylen -= 1
            else:
                z = y
                for xx in y_to_x.pop(z):
                    x_to_y[xx].discard(z)
                    x_minus[z] += 1
                    xlen -= 1

            if xlen > 0:
                heapq.heappush(x_len, [xlen, x])
            if ylen > 0:
                heapq.heappush(y_len, [ylen, y])
            ans += 1
        print(ans)


if __name__ == "__main__":
    main()
