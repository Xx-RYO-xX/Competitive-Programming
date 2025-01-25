import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    xs = []
    ys = []
    for _ in range(3):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    cx = Counter(xs)
    cy = Counter(ys)
    ans_x = [x for x, count in cx.items() if count == 1][0]
    ans_y = [y for y, count in cy.items() if count == 1][0]
    print(ans_x, ans_y)


if __name__ == '__main__':
    sys.exit(main())
