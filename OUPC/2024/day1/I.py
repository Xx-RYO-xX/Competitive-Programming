import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import numpy as np  
    from math import sqrt
    
    def dist(lst1, lst2):
        res=0
        for i in range(3):
            res=(lst1[i]-lst2[i])**2
        return sqrt(res)

    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        xyz1 = list(map(int, input().split()))
        xyz2 = list(map(int, input().split()))
        
        ans = float("inf")
        
        teimenn1 = -1
        teimenn2 = -1
        for i in range(3):
            if xyz1[i] == 0:
                teimenn1 = i
            if xyz2[i] == 0:
                teimenn2 = i
        
        if teimenn1 == -1:
            teimenn1 = 3
        if teimenn2 == -1:
            teimenn2 == 3
        
        if teimenn1 == teimenn2 == 3:
            ans = dist(xyz1, xyz2)

        if teimenn1 == 3:
            teimenn1, teimenn2 = teimenn2, teimenn1
            xyz1, xyz2 = xyz2, xyz1
        
        if teimenn1 == 0:
            

if __name__ == '__main__':
    main()
