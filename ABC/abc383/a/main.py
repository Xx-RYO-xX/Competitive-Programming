import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    t = []
    v = []
    for i in range(n):
        tt, vt = map(int, input().split())
        t.append(tt)
        v.append(vt)

    water = 0
    time = 0
    for i in range(n):
        elapsed = t[i] - time
        if water > 0:
            water -= elapsed
            if water < 0:
                water = 0
        water += v[i]
        time = t[i]

    print(water)
    


if __name__ == '__main__':
    main()
