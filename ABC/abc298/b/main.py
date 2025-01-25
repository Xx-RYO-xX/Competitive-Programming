import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import numpy as np
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    a = np.array(a)
    b = []
    for _ in range(n):
        b.append(list(map(int, input().split())))
    
    for _ in range(4):
        cond = True
        for i in range(n):
            for j in range(n):
                if a[i][j] == 1:
                    if b[i][j] == 1:
                        pass
                    else:
                        print(a)
                        print(b)
                        print()
                        cond = False
        if cond:
            print("Yes")
            exit()
        np.rot90(a)
    print("No")


if __name__ == '__main__':
    main()
