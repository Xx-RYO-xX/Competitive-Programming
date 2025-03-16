import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import math
    n = int(input())
    maxd = int((4*n)**(1/3))
    for d in range(1, 2*maxd):
        if n % d != 0:
            continue
        
        k = n//d
        hannbetu = 12*k - 3*d*d  
        if hannbetu < 0:
            continue
        
        t = int(math.isqrt(hannbetu))
        if t*t != hannbetu:
            continue
        
        if (t-3*d)%6 != 0:
            continue
        
        y = (t-3*d)//6
        if y <= 0:
            continue
        
        x = y+d
        print(x, y)
        return
    print(-1)


if __name__ == '__main__':
    sys.exit(main())
