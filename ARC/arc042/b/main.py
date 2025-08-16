import sys 


def input():return sys.stdin.readline().rstrip()

# https://tech.aru-zakki.com/python-line-dot-distance/
def calc_vector(x0, y0, x1, y1) :
    return x1-x0, y1-y0

def calc_dist(dot, line):
    ax, ay = dot
    bx, by, cx, cy = line 
    BAx, BAy = calc_vector(bx, by, ax, ay)
    BCx, BCy = calc_vector(bx, by, cx, cy)
    CAx, CAy = calc_vector(cx, cy, ax, ay)
    CBx, CBy = calc_vector(cx, cy, bx, by)

    if BAx * BCx + BAy * BCy < 0 :
        return (BAx * BAx + BAy * BAy)**0.5
    if CAx * CBx + CAy * CBy < 0 :
        return (CAx * CAx + CAy * CAy)**0.5
    
    s = abs(BAx * BCy - BAy * BCx)
    l = (BCx*BCx + BCy * BCy)**0.5
    return s/l


def main():
    X, Y = map(int, input().split())
    n = int(input())
    dot_lst = []
    for _ in range(n):
        x, y = map(int, input().split())
        dot_lst.append((x, y))

    bx, by = dot_lst[0]
    ans = calc_dist((X, Y), (bx, by, *dot_lst[-1]))
    for dot in dot_lst[1:]:
        # print(dot)
        x, y = dot
        ans = min(ans, calc_dist((X, Y), (bx, by, x, y)))
        bx, by = x, y
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
