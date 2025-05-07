import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import numpy as np
    
    n = int(input())
    s = []
    for _ in range(n):
        s.append(list(input()))
    s = np.array(s)
    
    t = []
    for _ in range(n):
        t.append(list(input()))
    t = np.array(t)
    
    ans = float("inf")
    for ii in range(4):
        rs = np.rot90(s, -ii)  
        diff = 0
        for i in range(n):
            for j in range(n):
                if rs[i][j] != t[i][j]:
                    diff += 1
        ans = min(ans, diff+ii)


    print(ans)

if __name__ == '__main__':
    sys.exit(main())
