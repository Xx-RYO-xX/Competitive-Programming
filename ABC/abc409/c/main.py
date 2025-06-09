import sys
from collections import Counter


def input():return sys.stdin.readline().rstrip()


def main():
    n, l = map(int, input().split())
    d = list(map(int, input().split()))
    
    if n < 3 or l % 3 != 0:
        print(0)
        return

    k = l//3
    s = [0]*n
    for i in range(1, n):
        s[i] = (s[i-1]+d[i-1])%l
    # print(s)

    pos = Counter(s)
    # print(pos)
    total = 0
    for x, c_x in pos.items():
        y = (x+k)%l
        z = (x+2*k)%l
        c_y = pos.get(y, 0)
        c_z = pos.get(z, 0)
        if c_y and c_z:
            total += c_x*c_y*c_z

    print(total//3)


if __name__ == '__main__':
    main()